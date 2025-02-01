import re
import os


class TextAnalizator:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(file=self.file, mode='r', encoding='utf-8') as file_str:
            text = file_str.read()
        return text

    def count_str(self):
        text = self.read_file()
        text_list = text.split('\n')
        count_str = len(text_list)
        return count_str

    def count_sim(self):
        text = self.read_file()
        count_sim = len(text)
        return count_sim

    def count_worlds(self):
        text = self.read_file()
        text_list = re.split('[\n ]', text)
        count_worlds = len(text_list)
        return count_worlds

    @staticmethod
    def check_file(file_name):
        if os.path.exists(file_name):
            print('Файл готов к работе')
        else:
            raise ValueError('Файла не существует!!')

    def write_file(self):
        file.check_file(self.file)
        with open(file='text_analyz_class.txt', mode='w', encoding='utf-8') as analise:
            analise.write(self.read_file() + '\n')
            analise.write(f'Кол-во строк в тексте: {self.count_str()}\n')
            analise.write(f'Кол-во символов в тексте: {self.count_sim()}\n')
            analise.write(f'Кол-во слов в тексте: {self.count_worlds()}\n')

file = TextAnalizator('lorem_ipsum.txt')
file.write_file()
