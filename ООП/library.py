import datetime


class Book:
    _GENRE = ('Комедия','Драма','Детектив','Романтика','Фантастика')
    def __init__(self, name, autor_name, year):
        self.name = name
        self.autor_name = autor_name
        self.year = year
        self.genre =''
        self.isbn = '000-0-0000-0000-0'

    def get_info(self):
        return f'{self.name} - {self.autor_name} ({self.year})'

    def is_older_then(self,year):
        if isinstance(year, int):
            if year <= self.year:
                return False
            else:
                return True
        else:
            return 'Год должен быть числом'

    def update_year(self, new_year):
        if isinstance(new_year, int):
            self.year = new_year
        else:
            raise ValueError('Год должен быть числом!')

    def set_genre(self, genre):
        if genre in Book._GENRE:
            self.genre = genre
        else:
            raise ValueError('Неизвестный жанр!')

    def set_isbn(self, isbn):
        if isinstance(isbn, int):
            isbn = str(isbn)
            if len(isbn) == 13:
                self.isbn = f'{isbn[0:3]}-{isbn[3]}-{isbn[4:8]}-{isbn[8:12]}-{isbn[12]}'
            else:
                raise ValueError('Число не соответствует формату ISBN')
        else:
            raise ValueError('ISBN должно быть числом!')

    def get_age(self):
        today_year = datetime.date.today().year
        return f'Книге {today_year - self.year} лет'

    def compare_books(self, other_book):
        if self.year > other_book.year:
            return f'Книга {other_book.name} старше книги {self.name}'
        elif self.year < other_book.year:
            return f'Книга {self.name} старше книги {other_book.name}'
        else:
            'Книги одного года выпуска'

roman = Book('love and honey', 'N.N.', 2021)
comedy = Book('hihanki da hahanki', 'Unknown', 1985)
print(roman.get_info())
print(roman.is_older_then('1998'))
roman.update_year(2020)
print(roman.year)
roman.set_genre('Романтика')
print(roman.genre)
roman.set_isbn(9782266111560)
print(roman.isbn)
print(roman.get_age())
print(roman.compare_books(comedy))
