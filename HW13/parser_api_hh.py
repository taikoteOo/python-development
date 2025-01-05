import requests
import json
import datetime as dt

def get_vacancies_pages(url: str):
    area = 2
    per_page = 100
    text = 'python'

    params = {
        'area': area,
        'per_page': per_page,
        'text': text
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data['pages'], data['found']

def get_data_page(url: str, page: int):
    params = {
        'area': 2,
        'per_page': 100,
        'page': page,
        'text': 'python'
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data

def parse_page(data: dict) -> dict:
    vacancies = {}
    items = data['items']
    for i in items:
        id_1 = i['id']
        vacancies[id_1] = {}
        vacancies[id_1]['Название'] = i['name']
        if i.get('address'):
            if i['address'].get('raw'):
                address = i['address']['raw']
                vacancies[id_1]['Адрес'] = address
            if i['address'].get('metro') and i['address']['metro'].get('station_name'):
                metro = i['address']['metro']['station_name']
                vacancies[id_1]['Станция метро'] = metro
        date = dt.datetime.strptime(i['published_at'][0:10], '%Y-%m-%d').date().strftime('%d.%m.%Y')
        #Тут можно было бы и срезом обойтись, но мне хотелось, чтобы дата смотрелась привычнее
        vacancies[id_1]['Дата публикации'] = date
        url = i['alternate_url']
        vacancies[id_1]['url'] = url
        if i.get('snippet') and i['snippet'].get('requirement'):
            snippet = i['snippet']['requirement']
            vacancies[id_1]['Требования'] = snippet
        if i.get('salary'):
            vacancies[id_1]['Заработная плата'] = {}
            if i['salary'].get('from'):
                fro = i['salary']['from']
                vacancies[id_1]['Заработная плата']['От'] = fro
            if i['salary'].get('to'):
                t = i['salary']['to']
                vacancies[id_1]['Заработная плата']['До'] = t
            currency = i['salary']['currency']
            vacancies[id_1]['Заработная плата']['Валюта'] = currency
            if i.get('experience') and i['experience'].get('name'):
                experience = i['experience']['name']
                vacancies[id_1]['Требуемый опыт'] = experience
    return vacancies

def main():
    vacancies = {}
    url_api = 'https://api.hh.ru/vacancies'
    pages, found  = get_vacancies_pages(url=url_api)
    print(f'Найдено {found} вакансий')
    for i in range(1, pages):
        data_page = get_data_page(url=url_api, page=i)
        page = parse_page(data_page)
        vacancies = {**vacancies, **page}
    return vacancies

def pages_to_json(data: dict) -> None:
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    all_vacancies = main()
    pages_to_json(all_vacancies)

# ПОЛУЧИТЬ: id, название, адрес (полный и станция метро), дата публикации (без времени), ссылка (alternate_url), требования (requirement in snippet), опыт и т.д.