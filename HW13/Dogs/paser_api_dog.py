import requests
import os
from random import randint


def get_image_link(url: str) -> str:
    resp = requests.get(url)
    data = resp.json()
    link = data.get('message')
    return link

def download_image(url: str) -> None:
    breed = url.split('/')[4]
    resp = requests.get(url)
    image = resp.content
    if not os.path.exists(breed):
        os.makedirs(breed, exist_ok=True)
    num = randint(1,1000)
    while not f'{breed}/{breed}_img_{num}.jpg':
        num = randint(1,1000)
    with open(f'{breed}/{breed}_img_{num}.jpg', 'wb') as f:
        f.write(image)

def all_dogs(url: str) -> None:
    for i in range(1,31):
        link = get_image_link(url=api_url)
        download_image(url=link)

api_url = 'https://dog.ceo/api/breeds/image/random'
all_dogs(api_url)

