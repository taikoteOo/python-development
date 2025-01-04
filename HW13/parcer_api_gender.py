from os import write

import requests

def get_gender_name(name: str) -> dict:
    url = 'https://api.genderize.io'
    params = {
        'name': name
    }
    resp = requests.get(url, params=params) #params - передаёт параметры в url
    data = resp.json()
    return data

def get_names_data(names: list) -> str:
    peoples = ''
    for name in names:
        pers = get_gender_name(name)
        if pers['gender'] == 'female':
            sex = 'женский'
        elif pers['gender'] == 'male':
            sex = 'мужской'
        else:
            sex = 'не определён'
        if pers['probability'] == 0.0:
            probability = 'не определена\nНекорректное имя!'
        else:
            probability = f'{int(pers['probability']*100)}%'
        persona = f'Имя - {name}\nПол - {sex}\nВероятность - {probability}\n\n'
        peoples += persona
    peoples =peoples.strip()
    return peoples

def parse_gender_data(data: list) -> None:
    with open('names.txt', 'w', encoding='utf-8') as f:
        f.write(get_names_data(data))

names = ['Елена','Владимир','3453456','Саша','авыавыаыенг']
parse_gender_data(names)