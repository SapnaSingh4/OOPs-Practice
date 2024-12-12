#Library Management system
#book class
class Book:
    def __init__(self, book_id, title, author, genre, available, edition):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.edition = edition

    def borrow_book(self):
        if self.available > 0:
            self.available -= 1
            print("Book borrowed successfully")
        else:
            print("Book not available")

    def return_book(self):
        self.available += 1
        print("Book returned successfully")

    def display_info(self):
        print(f"""
        Title: {self.title}
        Author: {self.author}
        Genre: {self.genre}
        Available: {self.available}
        Edition: {self.edition}
        """)

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.book_borrowed = []
        self.book_returned = []

    def borrow(self, book):
        if book in self.book_borrowed:
            print("Book already borrowed")
        else:
            book.borrow_book()
            self.book_borrowed.append(book)
            print("Book borrowed successfully")

    def return_book(self, book):
        if book in self.book_borrowed:
            book.return_book()
            self.book_borrowed.remove(book)
            self.book_returned.append(book)
            print("Book returned successfully")
        else:
            print("Book not borrowed")

    def view_info(self):
        print(f"""Borrowed Books by {self.user_name}: {[book.title for book in self.book_borrowed]}
Returned Books by {self.user_name}: {[book.title for book in self.book_returned]}
        """)

class Admin(User):
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book_id):
        library.remove_book(book_id)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    def view(self):
        for book in self.books:
            book.display_info()




# Creating books
book1 = Book(1, "The Hunger Game", "Suzanne Collins", "Fiction", 3, "1st Edition")
book2 = Book(2, "1984", "George Orwell", "Fiction", 2, "2nd Edition")
book3 = Book(3, "Pride and Prejudice", "Jane Austen","Fiction", 5, "3rd Edition")

# Creating a library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Creating a user
user1 = User(1, "Rein")
user2 = User(2,"Sapna")

# User borrowing books
user1.borrow(book1)
user1.borrow(book2)
user2.borrow(book3)

# User viewing borrowed books
user1.view_info()
user2.view_info()

# User returning books
user1.return_book(book1)
user1.return_book(book2)

# User viewing returned books
user1.view_info()

# Admin actions
admin = Admin(2, "Admin")
admin.add_book(library, Book(4, "The da vinci code", "Dan Brown", "Fiction", 7, "4th Edition"))
admin.remove_book(library, 2)

# View all books in the library
library.view()
