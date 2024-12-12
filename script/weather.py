import json

import requests
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent


def get_html(url: str) -> str | None:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
    # headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1'}
    # headers = {'User-Agent': UserAgent().chrome}
    try:
        response = requests.get(url, headers=headers)
        # Если успешний запрос ИЛИ переадресация, то хорошо
        if response.status_code == 200 or str(response.status_code)[0] == '3':
            html = response.text
            return html
        else:
            print(f'Ошибка запроса. Код ответа: {response.status_code}')
            return None
    except ConnectionError as err:
        print(f'Ошибка запроса.\n{err}')
        return None

def get_weather_from_day(html: str) -> dict:
    soup = Bs(html, 'html.parser')
    weather_info = {}
    day = soup.find('div', class_='dates short-d').text
    weather_info[day] = {}
    table = soup.find('div', class_='weather-short').find('table')
    table_rows = table.find_all('tr')
    for row in table_rows:
        weather_day = row.find('td', class_='weather-day').text
        weather_info[day][weather_day] = {}

        weather_temperature = row.find('td', class_='weather-temperature').text
        weather_typy = row.find('div', class_='wi')['title']
        weather_feeling = row.find('td', class_='weather-feeling').text
        weather_probability = row.find('td', class_='weather-probability').text

        weather_info[day][weather_day]['weather_temperature'] = weather_temperature
        weather_info[day][weather_day]['weather_typy'] = weather_typy
        weather_info[day][weather_day]['weather_feeling'] = weather_feeling
        weather_info[day][weather_day]['weather_feeling'] = weather_probability
    return weather_info

def write_data_to_json(data: dict) -> None:
    with open('weather.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

URL = 'https://world-weather.ru/pogoda/russia/saint_petersburg/7days/'
html = get_html(url=URL)

# for _ in range(10):
#     print(UserAgent().random) # Генерирует случайный Юзер Агент
#
if html:
    data = get_weather_from_day(html)
    write_data_to_json(data)

# print(get_weather_from_day(html))