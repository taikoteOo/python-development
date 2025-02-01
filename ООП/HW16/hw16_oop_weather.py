import requests
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError


class WeatherParser:
    def __init__(self, url):
        self.url = url
        self.html = ''
        self.data_weather = ''

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

    def today_weather(self):
        self.pars_html()
        today = self.data_weather[0]
        self.day_weather(today)

    def day_weather(self, day):
        weather_day = day.find('td', class_='weather-day').text
        weather_temperature = day.find('td', class_='weather-temperature').text
        weather_typy = day.find('div', class_='wi')['title']
        weather_feeling = day.find('td', class_='weather-feeling').text
        weather_probability = day.find('td', class_='weather-probability').text
        weather_pressure = day.find('td', class_='weather-pressure').text
        wind_direction = day.find_all('span', class_='tooltip')[0]['title']
        wind_speed = day.find('td', class_='weather-wind').text.strip()
        weather_humidity = day.find('td', class_='weather-humidity').text

        weather_info = f'Сегодня, {weather_day} в Санкт-Петербурге:\n'
        return weather_info

URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
weather = WeatherParser(URL)
weather.today_weather()