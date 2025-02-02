from api_library import Book, Library


library = Library()

book_1 = Book(title='Капитанская дочка', autor='А.С.Пушкин', year=1836, genre='Роман')
book_2 = Book(title='Герой нашего времени', autor='М.Ю.Лермонтов', year=1836, genre='Роман')

library.add_book(book_1)
library.add_book(book_2)

books = library.get_books()
for id_, book in books.items():
    print(book.get_info())