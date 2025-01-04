import requests

def get_gender_name(name: str) -> dict:
    # url = f'https://api.genderize.io/?name={name}'
    url = 'https://api.genderize.io'
    params = {
        'name': name
    }
    resp = requests.get(url, params=params) #params - передаёт параметры в url
    data = resp.json()
    return data

def parse_gender_data(data: dict) -> None:
    pass

gender_data = get_gender_name(name='Alena')
parse_gender_data(gender_data)