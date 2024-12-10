import requests
import json
from bs4 import BeautifulSoup as Bs


def get_html(url: str) -> str|None:
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200 and str(status)[0] != 3:
            print(f'Ошибка запросаю Код ошибки - {status}')
            return None
        print(f'Код ответа - {status}')
        html = response.text
        return html
    except requests.ConnectionError as error:
        print('Нет ответа от сервера')
        print(error)
        return None

def parse_html(html: str):
    courses = {}
    soup: Bs = Bs(html, 'html.parser')
    current_date = soup.find('h2', class_='h2 blue').text.split('\n')[-1].strip()[:10]
    table = soup.find('div', class_='module-tableSort')
    rows = table.findAll('tr')[2:]
    courses[current_date] = {}

    for row in rows:
        if not row.find('td', class_='t-center'):
            continue
        code = row.find('td', class_='t-center').text
        number_code = code.split()[0]
        txt_code = code.split()[1]

        name = row.find('td', class_='t-left').text.split('\n')[0]
        value = row.find('td', class_='t-right').text.strip()
        print(f'{number_code}-{txt_code} {name} {value}')

        courses[current_date][txt_code] = {
            'number_code': number_code,
            'name': name,
            'value': value
        }
    return courses

def write_data_to_json(data: dict) -> None:
    with open('couses.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_data_from_json(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

URL = 'https://www.alta.ru/currency/'
html = get_html(URL)
if html:
    courses = parse_html(html)
    write_data_to_json(data=courses)

courses_from_file = get_data_from_json('couses.json')
print(courses_from_file)