import json

import requests
from bs4 import BeautifulSoup as Bs

class Parser:
    def __init__(self, url):
        self.url = url
        self.data_weather = {}
        self.data_vacansies = []

    def get_html(self):
        response = requests.get(self.url)
        self.html = response.text
        # html= response.text
        # return html

    def pars_html(self):
        self.get_html()
        soup = Bs(html, 'parser.html')
        data = soup.find_all('table', class_='weather' )
        self.data_weather = {'data':data}
        # return data

    def write_data_to_file(self):
        with open('file.json', 'w') as f:
            json.dump(self.data_weather, f, indent=2)


parser_weather = Parser(url='www.weather.com')
parser_weather.pars_html()
# html = parser_weather.get_html()
# data = parser_weather.pars_html(html)
# parser_weather.get_html()

