from . import Book


class Library:
    id_ = 1
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if isinstance(book, Book):
            self.books[Library.id_] = book
            Library.id_ += 1

    def get_book_info(self, book_id):
        return self.books.get(book_id)

    def get_books(self):
        return self.books
