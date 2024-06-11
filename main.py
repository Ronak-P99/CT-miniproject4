import re 
from Book_operation import BookOperation, Book
from Book_operation import UserOperation, User
from Book_operation import AuthorOperation, Author
from Book_operation import GenreOperation, Genre
from connect_mysql import connect_database

#MODULE 5 SQL Mini Project functions:
def add_book_sql(name, author_name, genre_name, isbn, pub_date, status):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM authors WHERE name = %s", (author_name,))
            author_id = cursor.fetchone()
            if author_id is None:
                raise ValueError("Author not found. Please add the author before adding the book.")
            author_id = author_id[0]

            # Find the genre_id for the given genre_name
            cursor.execute("SELECT id FROM genres WHERE name = %s", (genre_name,))
            genre_id = cursor.fetchone()
            if genre_id is None:
                print(genre_name)
                raise ValueError("Genre not found. Please add the genre before adding the book.")
            genre_id = genre_id[0]
            
            query = """
            INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, author_id, genre_id, isbn, pub_date, status))
            
            conn.commit()
            print("Book added successfully.")
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def add_user_sql(name, library_id,):
    #Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            #SQL query  
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            
            #Executing the query
            cursor.execute(query, (name, library_id))

            conn.commit()
            print("User and session logged successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def add_borrowed_books_sql(user_name, book_name, borrow_date, return_date):
    #Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM users WHERE name = %s", (user_name,))
            user_id = cursor.fetchone()
            if user_id is None:
                raise ValueError("User not found. Please add the User Name first.")
            user_id = user_id[0]

            cursor.execute("SELECT id FROM books WHERE title = %s", (book_name,))
            book_id = cursor.fetchone()
            if book_id is None:
                raise ValueError("Book not found. Please add the Book Name first.")
            book_id = book_id[0]
            
            #SQL query  
            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
            
            #Executing the query
            cursor.execute(query, (user_id, book_id, borrow_date, return_date))
        
            conn.commit()
            print("Author and session logged successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def add_author_sql(name, bio):
    #Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            #SQL query  
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            
            #Executing the query
            cursor.execute(query, (name, bio))
        
            conn.commit()
            print("Author and session logged successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def add_genre_sql(name, desc, category):
    #Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            #SQL query
            query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
            
            #Executing the query
            cursor.execute(query, (name, desc, category))
        
            conn.commit()
            print("Member and session logged successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

def updated_book_sql(name, status):
      #Establishing the connection
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if status == 0:
                #SQL query
                query = "UPDATE books SET availability = %s WHERE title = %s"

                #Executing the query
                cursor.execute(query, (status, name))
                conn.commit()
                print("Availability updated successfully.")
            
            if status == 1:
                #SQL query
                query = "UPDATE books SET availability = %s WHERE title = %s"

                #Executing the query
                cursor.execute(query, (status, name))
                conn.commit()
                print("Availability updated successfully.")
        
        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()




def main():
    book_inst = BookOperation()
    user_inst = UserOperation()
    author_inst = AuthorOperation()
    genre_inst = GenreOperation()
    while True:
        try:
            action = int(input("\nWlecome to the Library Management System!\n\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit\nChoose the number you would like: "))
            if action not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid action.")
            
            #!!BOOK OPERATION!!

            if action == 1:
                try:
                    while True:
                        print("Book Operations:\n\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4, 5]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please enter the name of the book: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            author = input("Please enter the name of the author: ")
                            if all([letter.isalpha() or letter.isspace() for letter in author]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            isbn = input("Please enter the ISBN of the book (Do not format!): ")
                            try:
                                int(isbn)
                                formatted_isbn = re.sub(r'(\d{3})(\d{10})', r'\1-\2', isbn)
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            genre = input("Please enter the genre of the book: ")
                            if all([letter.isalpha() or letter.isspace() for letter in genre]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            date = input("Please enter the date the book was published (Do not format!): ")
                            try:
                                int(date)
                                formatted_date = re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3-\1-\2', date)
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            status = 'Available'
                            book_inst.add_book(Book(name, author, formatted_isbn, genre, formatted_date), status)
                            #SQL COMMAND
                            add_book_sql(name, author, genre, formatted_isbn, formatted_date, 1)
                        elif action == 2:
                            user_name = input("Enter the name of the user: ")
                            name = input("Enter book name to borrow: ")
                            date1 = input("Please enter the date the book was borrowed (Do not format!): ")
                            date2 = input("Please enter the date you would like to return the book (Do not format!): ")
                            try:
                                int(date1)
                                formatted_date1 = re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3-\1-\2', date1)
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            try:
                                int(date2)
                                formatted_date2 = re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3-\1-\2', date2)
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            book_inst.borrow_book(name)
                             #SQL COMMAND
                            updated_book_sql(name, 0)
                            add_borrowed_books_sql(user_name, name, formatted_date1, formatted_date2)
                        elif action == 3:
                            name = input("Enter book name to return: ")
                            book_inst.return_book(name)
                            #SQL COMMAND
                            updated_book_sql(name, 1)
                        elif action == 4:
                            name = input("Enter the name of the book you would like to search for: ")
                            book_inst.search_book(name)
                        elif action == 5:
                            book_inst.display_books()
                        elif action == 6:
                            break
                except ValueError as e:
                    print(e)

            #!!USER OPERATION!!

            if action == 2:
                try:
                    while True:
                        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n4. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please enter the name of the user: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            lib_id = input("Please enter the 10 digit library ID: ")
                            try:
                                if len(lib_id) == 10:
                                    int(lib_id)
                                else:
                                    print("Library ID needs to be a length of 10!")
                                    break
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            borrowed_books = []
                            while True:
                                book = input("What books has the user borrowed? Type 'Stop' once done listing! ")
                                if book.lower() != 'stop':
                                    borrowed_books.append(book) 
                                else: 
                                    break     
                            user_inst.add_user(User(name, lib_id, borrowed_books))
                             #SQL COMMAND
                            add_user_sql(name, lib_id,)
                        elif action == 2:
                            user_input = input("What is the name of the person you would like to see the details of? (Please make sure to type it exactly as in the system!): ")
                            user_inst.view_user(user_input)
                        elif action == 3:
                            user_inst.view_all()
                        elif action == 4:
                            break
                except ValueError as e:
                    print(e)

            #!!Author Operations!!

            if action == 3:
                try:
                    while True:
                        print("\nAuthor Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please enter the name of the author: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            author_biography = input("Please enter a brief description of the author in 250 chars or less.\n")
                            if len(author_biography) >= 251:
                                print("Please make sure the biography is less than 250 characters!")
                                break
                            author_inst.add_author(Author(name, author_biography))
                            #SQL COMMAND
                            add_author_sql(name, author_biography)
                        elif action == 2:
                            author_input = input("What is the name of the author you would like to see the details of? (Please make sure to type it exactly as in the system!): ")
                            author_inst.view_author(author_input)
                        elif action == 3:
                            author_inst.view_all_author()
                        elif action == 4:
                            break
                except ValueError as e:
                    print(e)

            #!!Genre Operations!!

            if action == 4:
                try:
                    while True:
                        print("\nGenre Operations\n1. Add a new genre\n2. View genre details\n3. Display all genres\n4. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please give the name of the genre out of this list: 'HORROR', 'THRILLER', 'COMEDY', 'FANTASY', 'ACTION', 'DRAMA': ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            genre_description = input("Please enter a brief description of the genre in 100 characters or less.\n")
                            if len(genre_description) >= 101:
                                print("Please make sure the description is less than 100 characters!")
                                break
                            categories = ['HORROR', 'THRILLER', 'COMEDY', 'FANTASY', 'ACTION', 'DRAMA, NONFICTION, FICTION']
                            category = input("Choose the category out of this list: Nonfiction or Fiction: ")
                            if name.upper() in categories and category.upper in categories: 
                                genre_inst.add_genre(Genre(name, genre_description, category))
                                #SQL COMMAND
                                add_genre_sql(name, genre_description, category)
                            else:
                                print("The category you provided was not in the list. Please try again.")
                                break
                        elif action == 2:
                            name = input("Please give the name of the book to check the genre. (Please make sure to type it exactly as in the system!): ")
                            genre_inst.view_genre(name)
                        elif action == 3:
                            genre_inst.view_all_genres()
                        elif action == 4:
                            break
                except ValueError as e:
                    print(e)
            
            if action == 5:
                break
                
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()