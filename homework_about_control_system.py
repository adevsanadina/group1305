from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, author_or_director, year):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"


class Book(LibraryItem):
    def __init__(self, title, author, year, number_of_pages):
        super().__init__(title, author, year)
        self.number_of_pages = number_of_pages

    def description(self):
        base_description = super().description()
        return f"{base_description}, Number of pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def description(self):
        base_description = super().description()
        return f"{base_description}, Issue number: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration

    def description(self):
        base_description = super().description()
        return f"{base_description}, Duration: {self.duration} minutes"


book = Book("War and Peace", "Lev Tolstoy", 1869, 1225)
magazine = Magazine("National Geographic", "Various Authors", 2023, 502)
dvd = DVD("Inception", "Christopher Nolan", 2010, 148)

print(book.description())
print(magazine.description())
print(dvd.description())

