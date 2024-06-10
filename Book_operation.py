from Lib_management import Book
from Lib_management import User
from Lib_management import Author
from Lib_management import Genre
from connect_mysql import connect_database

class BookOperation:
    def __init__(self):
        self.books = {}

    def add_book(self, book, status):
        if book.title in self.books:
            self.books[book.title]['status'] = status
        else:
            self.books[book.title] = {'book': book, 'status': status}
           
    
    def borrow_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name]["status"] == 'Available':
                self.books[book_name]["status"] = 'Not Available'
                print(f"You have successfully borrowed {book_name}!")
        else:
            print("Either the book was not in our system or the book is already borrowed!")
    
    def return_book(self, book_name):
        if book_name in self.books and self.books[book_name]["status"] == 'Not Available' :
            self.books[book_name]["status"] = 'Available'
            print(f"You have successfully returned {book_name}!")
        else:
            print("Either the book was not in our system or the book is already returned!")
        
    def search_book(self, book_name):
        if book_name in self.books:
            print(f"{book_name} has been found! Make sure to check the availability status!")
        else:
            print("We don't carry that book! Sorry!")
    
    def display_books(self):
        for book_title, details in self.books.items():
            book, status = details['book'], details['status']
            print(f"Title: {book_title} - Author: {book.author} - Publication date: {book.date} - Genre: {book.genre} - ISBN: {book.number} - Status: {status} ")

class UserOperation:
    def __init__(self):
        self.user = {}
    
    def add_user(self, user):
        if user.name not in self.user:
            self.user[user.name] = {'Library ID': user.id, 'Borrowed Books': user.books_borrowed}
    
    def view_user(self, inputted_user):
        if inputted_user in self.user:
            print(f"Name: {inputted_user} - Library ID: {self.user[inputted_user]["Library ID"]} - Borrowed Books: {self.user[inputted_user]["Borrowed Books"]}")
        else:
            print("User not found in system! Make sure the name provided is exactly the same!")
    
    def view_all(self):
        for user_name, details in self.user.items():
            name, books = details['Library ID'], details['Borrowed Books']
            print(f"Name: {user_name} - Library ID: {name} - Borrowed Books: {books}")

class AuthorOperation:
    def __init__(self):
        self.author = {}
    
    def add_author(self, author):
        if author.name not in self.author:
            self.author[author.name] = {'Biography': author.bio}
    
    def view_author(self, inputted_author):
        if inputted_author in self.author:
            print(f"Name: {inputted_author} - Author Biography: {self.author[inputted_author]["Biography"]}")
        else:
            print("Author not found in system! Make sure the name provided is exactly the same!")

    def view_all_author(self):
        for author_name, details in self.author.items():
            author = details['Biography']
            print(f"Name: {author_name} - Biography: {author}")

class GenreOperation:
    def __init__(self):
        self.genre = {}
    
    def add_genre(self, genre):
        if genre.name not in self.genre:
            self.genre[genre.name] = {'Description': genre.desc, 'Category': genre.category}
    
    def view_genre(self, inputted_book):
        if inputted_book in self.genre:
             print(f"Name: {inputted_book} - Genre Description: {self.genre[inputted_book]["Description"]} - Category: {self.genre[inputted_book]["Category"]}")
        else:
            print("Book not found in system! Make sure the name provided is exactly the same!")

    def view_all_genres(self):
        for genre_name, details in self.genre.items():
            desc, category = details['Description'], details['Category']
            print(f"Name: {genre_name} - Description: {desc} - Category: {category}")




        

        



    


        