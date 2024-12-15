import requests
import json
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

def get_phon_prise(html: str):
    soup = Bs(html, 'html.parser')
    table = soup.find('div', class_='item_card')
    table_items = table.find_all('div', 'item')
    phone_price_j = {}
    phone_price = []
    for item in table_items:
        name = item.find('a', 'name_item').text
        price = item.find('p', 'price').text
        phone_price_j[name] = price
    for key in phone_price_j:
        phone_price.append(f'{key} - {phone_price_j[key]}')
    return '\n'.join(phone_price)


URL = 'https://parsinger.ru/html/index1_page_1.html'
html = get_html(url=URL)

if html:
    courses = get_phon_prise(html)

with open('hw9.txt', 'w', encoding='utf-8') as file:
    file.write(get_phon_prise(html))