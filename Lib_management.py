class Book:
    def __init__(self, title, author, book_number, genre, publication_date):
        self.title = title
        self.author = author
        self.number = book_number
        self.genre = genre
        self.date = publication_date

class User:
    def __init__(self, name, id, books_borrowed):
        self.name = name
        self.id = id
        self.books_borrowed = books_borrowed

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.bio = biography

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.desc = description
        self.category = category


   