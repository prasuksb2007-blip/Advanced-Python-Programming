"""
Write a program to create a simplified Library Management System using object-oriented
programming principles in Python. This system should manage books and patrons (library users),
allowing for basic operations such as adding new books, registering patrons, borrowing books, and
returning books.
"""
# Defining the Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        result = "Available" if not self.is_borrowed else "Borrowed"
        return(f"The Author of {self.title} Book ISBN:{self.isbn} is {self.author} | Status: {result}")
    
    def borrow_book(self):
        if self.is_borrowed:
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

# Defining the Patron class
class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.__patron_id = patron_id
        self.__borrowed_book = []

    def patron_id(self):
        return self.__patron_id
       
    def borrow_book(self, book):
        if book in self.__borrowed_book:
            return False
        self.__borrowed_book.append(book)
        return True

    def return_book(self, book):
        if book in self.__borrowed_book:
            self.__borrowed_book.remove(book)
            return True
        return False

# Defining the Libary class
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_patron(self, patron):
        self.patrons[patron.patron_id()] = patron

    def borrow_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print("Patron not found")
            return False

        if isbn not in self.books:
            print("Book Not found")
            return False

        book = self.books[isbn]
        patron = self.patrons[patron_id]

        if not book.borrow_book():
            print(f"Sorry, '{book.title}' is already borrowed.")
            return False
        
        if not patron.borrow_book(book):
            book.return_book()
            print(f"{patron.name} already has this book.")
            return False
        print(f"Success! {patron.name} borrowed '{book.title}'.")
        return True
            
    def return_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print("Patron not found")
            return False
        
        if isbn not in self.books:
            print("Book Not found")
            return False

        book = self.books[isbn]
        patron = self.patrons[patron_id]

        if not patron.return_book(book):
            print(f"{patron.name} did not borrow '{book.title}'.")
            return False
        book.return_book()
        print(f"Success! {patron.name} returned '{book.title}'.")
        return True

# Example usage
if __name__ == "__main__":
    library = Library()
    book = Book("Python Basics", "John Doe", "B001")
    print(book)
    patron1 = Patron("Alice", "P001")
    patron2 = Patron("Joe", "P002")
    library.add_book(book)
    library.register_patron(patron1)
    library.register_patron(patron2)
    
    library.borrow_book("P001", "B001")
    library.borrow_book("P002", "B001")
    library.return_book("P001", "B001")

"""
--> Output
The Author of Python Basics Book ISBN:B001 is John Doe | Status: Available
Success! Alice borrowed 'Python Basics'.
Sorry, 'Python Basics' is already borrowed.
Success! Alice returned 'Python Basics'.
"""