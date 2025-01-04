import requests
from random import randint #ф-ия, которая генерит случайное число randint(1,1000)


def get_image_link(url: str) -> str:
    resp = requests.get(url)
    data = resp.json()
    link = data.get('message')

    return link

def download_image(url: str) -> None:
    print(url)
    resp = requests.get(url)
    image = resp.content
    with open('../image.jpg', 'wb') as f:
        f.write(image)

api_url = 'https://dog.ceo/api/breeds/image/random'
link = get_image_link(url=api_url)
download_image(url=link)

# api/breeds = PATH-param (параметры пути)
# 'https://api.genderize.io?name=misha'
# ? -отделяет домен от QUERY-параметра
# name=misha - QUERY-param (параметр запроса)
# & - объединяет несколько параметров