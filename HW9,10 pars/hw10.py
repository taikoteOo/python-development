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

def get_a(html: str) -> dict:
    soup = Bs(html, 'html.parser')
    link_info = {}
    link_info['pagination'] = {}
    link_info['navigation'] = {}
    pagination = soup.find('div', 'pagen').find_all('a')
    navigation = soup.find('div', 'nav_menu').find_all('a')
    for pag in pagination:
        name = pag.text
        link = pag.get('href')
        link_info['pagination'][name] = link
    for nav in navigation:
        name = nav.text
        link = nav.get('href')
        link_info['navigation'][name] = link
    return link_info

def links_to_json(data: dict) -> None:
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

URL = 'https://parsinger.ru/html/index1_page_1.html'
html = get_html(url=URL)

if html:
    links = get_a(html)
    links_to_json(links)

