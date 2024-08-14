import pytest
from library import Library, Book


@pytest.fixture(scope="class")
def library():
    return Library("Central Library")


@pytest.fixture(scope="class")
def book1():
    return Book("1984", "George Orwell")


@pytest.fixture(scope="class")
def book2():
    return Book("To Kill a Mockingbird", "Harper Lee")


def test_add_book(library, book1):
    initial_count = len(library.books)
    library.add_book(book1)
    assert len(library.books) == initial_count + 1
    assert library.books[-1] == book1


def test_remove_book(library, book1):
    library.add_book(book1)
    initial_count = len(library.books)
    library.remove_book(book1)
    assert len(library.books) == initial_count - 1


def test_list_books(library, book1, book2):
    library.add_book(book1)
    library.add_book(book2)
    expected_books = [book1, book2]
    assert library.books == expected_books


