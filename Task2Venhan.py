from datetime import date, timedelta

class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity
        self.borrowed_count = 0

    def __str__(self):
        return f"{self.title} by {self.author}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def borrow_book(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.borrowed_count += 1
            return True
        else:
            return False

    def return_book(self):
        if self.borrowed_count > 0:
            self.borrowed_count -= 1
            self.quantity += 1

class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id

    def __str__(self):
        return f"{self.name} (ID: {self.membership_id})"

    def update_contact_details(self, new_contact_details):
        self.contact_details = new_contact_details

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def remove_borrower(self, borrower):
        if borrower in self.borrowers:
            self.borrowers.remove(borrower)

    def borrow_book(self, borrower_id, book):
        if book.borrow_book():
            if borrower_id in self.borrowed_books:
                self.borrowed_books[borrower_id].append(book)
            else:
                self.borrowed_books[borrower_id] = [book]

    def return_book(self, borrower_id, book):
        if borrower_id in self.borrowed_books and book in self.borrowed_books[borrower_id]:
            book.return_book()
            self.borrowed_books[borrower_id].remove(book)

    def search_books(self, keyword):
        result = []
        for book in self.books:
            if (keyword.lower() in book.title.lower() or
                keyword.lower() in book.author.lower() or
                keyword.lower() in book.genre.lower()):
                result.append(book)
        return result

    def show_available_books(self):
        for book in self.books:
            print(f"{book}: Available Quantity: {book.quantity}")

    def check_overdue_books(self, borrower_id):
        overdue_books = []
        today = date.today()
        for book in self.borrowed_books.get(borrower_id, []):
            due_date = today + timedelta(days=14)  # Assuming a 2-week borrowing period
            if due_date < today:
                overdue_books.append(book)
        return overdue_books
# Creating instances of books and borrowers
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780590353427", "Fantasy", 5)
book2 = Book("The Hobbit", "J.R.R. Tolkien", "9780618260300", "Fantasy", 3)

borrower1 = Borrower("John Doe", "john.doe@example.com", "ID001")
borrower2 = Borrower("Jane Smith", "jane.smith@example.com", "ID002")

# Creating a library instance
library = Library()

# Adding books and borrowers to the library
library.add_book(book1)
library.add_book(book2)

library.add_borrower(borrower1)
library.add_borrower(borrower2)

# Borrowing a book
library.borrow_book("ID001", book1)

# Returning a book
library.return_book("ID001", book1)

# Searching for books
results = library.search_books("Harry Potter")
for result in results:
    print(result)

# Showing available books
library.show_available_books()

# Checking overdue books for a borrower
overdue_books = library.check_overdue_books("ID001")
if overdue_books:
    print("Overdue books for borrower ID001:")
    for book in overdue_books:
        print(book)
else:
    print("No overdue books.")

