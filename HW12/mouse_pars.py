import requests
import json
from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError


# Программа, которая подтягивает данные обо всех компьютерных мышах с сайта parsinger.ru

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

def get_mouse_info(html: str):
    all_soup = Bs(html, 'html.parser')
    all_a = all_soup.find('div', 'pagen').find_all('a')
    all_mouse = {}
    for i in all_a:
        web = get_html(url='https://parsinger.ru/html/' + i['href'])
        num_web = i.text
        soup = Bs(web, 'html.parser')
        table = soup.find('div', class_='item_card')
        table_items = table.find_all('div', 'item')
        all_mouse[num_web] = {}
        for item in table_items:
            i = item.find('a')['href']
            url = get_html(url='https://parsinger.ru/html/' + i)
            soup_card = Bs(url, 'html.parser')
            name = soup_card.find('p').text
            all_mouse[num_web][name] = {}

            img = soup_card.find('img')['src']
            price = soup_card.find_all('span')[1].text
            all_mouse[num_web][name]['Изображение'] = img
            all_mouse[num_web][name]['Цена'] = price

            info = soup_card.find_all('li')
            for li in info:
                key = li.text.split(': ')[0]
                value = li.text.split(': ')[1]
                all_mouse[num_web][name][key] = value

            presence = soup_card.find_all('span')[0].text.split(': ')
            all_mouse[num_web][name][presence[0]] = presence[1]
    return all_mouse

def links_to_json(data: dict) -> None:
    with open('mouses.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

URL = 'https://parsinger.ru/html/index3_page_1.html'
html = get_html(url=URL)

if html:
    courses = get_mouse_info(html)
    links_to_json(courses)