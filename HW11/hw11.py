import json
import requests
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError


def get_html(url: str) -> str | None:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200 or str(response.status_code)[0] == '3':
            html = response.text
            return html
        else:
            print(f'Ошибка запроса. Код ответа: {response.status_code}')
            return None
    except ConnectionError as err:
        print(f'Ошибка запроса.\n{err}')
        return None

def get_weather_from_week(html: str) -> dict:
    soup = Bs(html, 'html.parser')
    weather_info = {}
    weather_days = soup.find_all('div', 'weather-short')
    for weather_day in weather_days:
        if weather_day.find('div', class_='dates short-d'):
            day = weather_day.find('div', class_='dates short-d').text
        else:
            day = weather_day.find('div', class_='dates short-d red').text
        weather_info[day] = {}
        table = weather_day.find('table')
        table_rows = table.find_all('tr')
        for row in table_rows:
            weather_day = row.find('td', class_='weather-day').text
            weather_info[day][weather_day] = {}

            weather_temperature = row.find('td', class_='weather-temperature').text
            weather_typy = row.find('div', class_='wi')['title']
            weather_feeling = row.find('td', class_='weather-feeling').text
            weather_probability = row.find('td', class_='weather-probability').text
            weather_pressure = row.find('td', class_='weather-pressure').text
            wind_direction = row.find_all('span', class_='tooltip')[0]['title']
            wind_speed = row.find('td', class_='weather-wind').text.strip()
            weather_humidity = row.find('td', class_='weather-humidity').text

            weather_info[day][weather_day]['weather_temperature'] = weather_temperature
            weather_info[day][weather_day]['weather_typy'] = weather_typy
            weather_info[day][weather_day]['weather_feeling'] = weather_feeling
            weather_info[day][weather_day]['weather-probability'] = weather_probability
            weather_info[day][weather_day]['weather-pressure'] = weather_pressure
            weather_info[day][weather_day]['weather-wind'] = {}
            weather_info[day][weather_day]['weather-wind']['wind-direction'] = wind_direction
            weather_info[day][weather_day]['weather-wind']['wind-speed'] = wind_speed
            weather_info[day][weather_day]['weather-humidity'] = weather_humidity
    return weather_info

URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
html = get_html(url=URL)

def write_data_to_json(data: dict) -> None:
    with open('weather.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if html:
    data = get_weather_from_week(html)
    write_data_to_json(data)
