import requests
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError


class WeatherParser:
    def __init__(self, url):
        self.url = url
        self.html = ''
        self.data_weather = None

    def get_html(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
        try:
            response = requests.get(self.url, headers=headers)
            response.encoding = 'utf-8'
            if response.status_code == 200 or str(response.status_code)[0] == '3':
                self.html = response.text
        except ConnectionError as err:
            print(f'Ошибка запроса.\n{err}')
            return None

    def pars_html(self):
        self.get_html()
        soup = Bs(self.html, 'html.parser')
        self.data_weather = soup.find_all('div', 'weather-short')

    @staticmethod
    def day_weather(day):
        if day.find('div', class_='dates short-d'):
            day_name = day.find('div', class_='dates short-d').text
        else:
            day_name = day.find('div', class_='dates short-d red').text

        table = day.find('table')
        times = table.find_all('tr')
        all_time = ''
        for time in times:
            weather_time = time.find('td', class_='weather-day').text
            weather_temperature = time.find('td', class_='weather-temperature').text
            weather_typy = time.find('div', class_='wi')['title']
            wind_speed = time.find('td', class_='weather-wind').text.strip()
            all_time += f'{weather_time}: {weather_temperature}C, {weather_typy}, Ветер {wind_speed} м/с\n'
        return day_name, all_time

    def today_weather(self):
        self.pars_html()
        today = self.data_weather[0]
        day_name, all_time = self.day_weather(today)
        weather_info = f'Сегодня, {day_name} в Санкт-Петербурге:\n{all_time}'
        return weather_info

    def tomorrow_weather(self):
        self.pars_html()
        tomorrow = self.data_weather[1]
        day_name, all_time = self.day_weather(tomorrow)
        weather_info = f'Завтра, {day_name} в Санкт-Петербурге:\n{all_time}'
        return weather_info

    def all_temp(self):
        self.pars_html()
        all_temp = []
        for day in self.data_weather:
            times = day.find_all('td', class_='weather-temperature')
            for time in times:
                temp = int(time.text[:-1])
                all_temp.append(temp)
        all_temp.sort()
        return all_temp

    def max_temp(self):
        all_temp = self.all_temp()
        max_temp = all_temp[-1]
        return f'Максимальная температура за неделю: {max_temp}°C'

    def min_temp(self):
        all_temp = self.all_temp()
        min_temp = all_temp[0]
        return f'Минимальная температура за неделю: {min_temp}°C'

    def write_file(self):
        with open(file='weather_class.txt', mode='w', encoding='utf-8') as weather_file:
            weather_file.write(self.today_weather() + '\n')
            weather_file.write(self.tomorrow_weather() + '\n')
            weather_file.write(self.max_temp() + '\n')
            weather_file.write(self.min_temp())


URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
weather = WeatherParser(URL)
weather.write_file()