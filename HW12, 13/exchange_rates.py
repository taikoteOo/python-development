import requests
import json
import datetime as dt
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError


# Программа, которая показывает данные о курсе Доллара США, Евро и Юаня по отношению к рублю за последние 3 дня
# Данные для этого домашнего задания были взяты с официального сайта Банка России

# На момент написания кода, официальный курс валют не обновлялся с 29 числа
# При запуске она подтянет последний день, данные от которого есть на сайте и два дня до него

today = dt.datetime.now().strftime('%d.%m.%Y')

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

def get_exchange_rates(html: str):
    soup_all = Bs(html, 'html.parser')
    date_str = soup_all.find('button', class_='datepicker-filter_button').text
    today = dt.datetime.strptime(date_str, '%d.%m.%Y').date()
    exchange_rates = {}
    for day in range(0,3):
        html1 = get_html(url=f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={dt.datetime.strftime((today - dt.timedelta(days=day)), '%d.%m.%Y')}')
        soup = Bs(html1, 'html.parser')
        date = soup.find('button', class_='datepicker-filter_button').text
        table = soup.find('table', class_='data').find_all('tr')
        exchange_rates[date] = {}
        for i in range(1, len(table)):
            tr = table[i]
            name = tr.find_all('td')[3].text
            num_code = tr.find_all('td')[0].text
            code = tr.find_all('td')[1].text
            rates = tr.find_all('td')[4].text

            if int(num_code) in [840,978,156]:
                exchange_rates[date][name] = {}
                exchange_rates[date][name]['Код валюты'] = code
                exchange_rates[date][name]['Курс'] = rates
    return exchange_rates

def links_to_json(data: dict) -> None:
    with open('exchange_rates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

URL = f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={today}'
html = get_html(url=URL)

if html:
    courses = get_exchange_rates(html)
    links_to_json(courses)