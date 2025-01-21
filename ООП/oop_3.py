"""
@classmethod - метод, который принимает ссылку на сам класс в качестве первого аргумента.
    Он может изменять состояние класса, а не конкретного экземпляра.
@staticmethod - метод, который не принимает ни ссылку на класс, ни ссылку на экземпляр в качестве аргумента.
     Он не может изменять состояние класса или экземпляра. Это просто функция, которая принадлежит классу, но не зависит от его состояния.
"""
import os


class Person:
    country_of_origin = 'russia'
    count = 0

    @staticmethod
    def check_exists_file(filename):
        if os.path.isfile(filename):
            return True
        raise  ValueError('File not exist')

    @classmethod
    def init_from_birthday(cls, name, birthday): # альтернативный конструктор с передачей года вместо возраста
        age = 2025 - birthday
        return cls(name, age) # Вернуть объект текущего класса

    @classmethod
    def edit_country(cls):
        cls.country_of_origin = cls.country_of_origin.title()

    @classmethod
    def increment_count(cls):
        cls.count += 1

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.increment_count() # Происходит внутри класса, счётчик кол-ва объектов класса

    @classmethod
    def get_object_count(cls):
        return cls.count

    def hello(self):
        print(f'My name is {self.name}')

    def  change_age(self, new_age):
        self.age = new_age

    def __add__(self, other):
        return self.age + other.age

    def __str__(self): # метод, который выводит объект на экран
        return f'{self.name} {self.age}' # переопределение (перегрузка) метода
        # return ''.join([self.name, self.age])

person = Person(name='Dima', age=25)
person_2 = Person.init_from_birthday(name='Elena', birthday=1990)
print(person) # <__main__.Person object at 0x7002060cbb80> - строковое представление объекта
print(person+person_2)