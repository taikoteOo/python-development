import uuid
from datetime import datetime


class Book:
    def __init__(self, title, autor, year, genre=None):
        """
        Конструктор класса Book
        :param title: Название книги
        :param autor: Автор книги
        :param year: ГОд издания
        :param genre: Жанр книги (по умолчанию None)
        :param isbn: ISBN книги (по умолчанию None)
        """
        self.title = title
        self.autor = autor
        self.genre = genre
        self.year = year
        self.__isbn = uuid.uuid4().hex[:9]

    def get_info(self):
        """
        Возвращает строку с информацией о книге
        :return: Строка с информацией о книге
        """
        info = f'{self.title} - {self.autor} ({self._year})'
        if self.genre:
            info += f', Жанр: {self.genre}'
        info += f', ISBN: {self.__isbn}'

        return info

    @staticmethod
    def is_valid_year(year):
        if isinstance(year, int):
            if datetime.today().year < year < 1445:
                return False
            else:
                return True
        elif isinstance(year, str):
            if year.isdigit():
                if datetime.today().year < int(year) < 1445:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def is_older_than(self, year):
        """
        Проверяет, была ли книга издана до указанного года
        :param year: Год издания
        :return: bool
        """
        if self.is_valid_year(year):
            return self._year < year
        else:
            raise ValueError('Неверное значение для года издания')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if self.is_valid_year(new_year):
            self._year = new_year
        else:
            raise ValueError('Неверное значение для года издания')

    def get_book_age(self):
        current_year = datetime.today().year
        return current_year - self._year


# book = Book(title='Капитанская дочка', autor='А.С.Пушкин', year=1836, genre='Роман')
# print(book.get_info())
# book.year = 1837
# print(book.year)
# print(book.get_book_age())
# print(book.is_older_than(year=1700))
