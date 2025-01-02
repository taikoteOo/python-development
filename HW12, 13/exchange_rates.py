import requests
import json
import datetime as dt
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

def get_exchange_rates(html: str):
    soup = Bs(html, 'html.parser')
    exchange_rates = {}



URL = 'https://www.cbr.ru/currency_base/daily'
html = get_html(url=URL)

today = dt.datetime.now() - dt.timedelta(days=1)
print(today.strftime('%d.%m.%Y'))
# if html:
#     courses = get_phon_prise(html)