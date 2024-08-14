

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'

    __repr__ = __str__


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f'Book {book} has been added to the library.')

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f'Book {book} has been removed from the library.')
        else:
            print(f'Book {book} is not in the library.')

    def list_books(self):
        if self.books:
            print(f'Books in {self.name}:')
            for book in self.books:
                print(f' - {book}')
        else:
            print(f'There are no books in {self.name}.')

    def __str__(self):
        return f'<Library {self.name}>'

    __repr__ = __str__




