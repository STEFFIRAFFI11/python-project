import json
import os

class Library:
    def _init_(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book_name):
        if book_name in self.books:
            print(f"The book '{book_name}' already exists in the library.")
        else:
            self.books[book_name] = "available"
            self.save_books()
            print(f"The book '{book_name}' has been added to the library.")

    def remove_book(self, book_name):
        if book_name in self.books:
            del self.books[book_name]
            self.save_books()
            print(f"The book '{book_name}' has been removed from the library.")
        else:
            print(f"The book '{book_name}' does not exist in the library.")

    def borrow_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name] == "available":
                self.books[book_name] = "borrowed"
                self.save_books()
                print(f"You have borrowed '{book_name}'.")
            else:
                print(f"The book '{book_name}' is currently borrowed.")
        else:
            print(f"The book '{book_name}' does not exist in the library.")

    def return_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name] == "borrowed":
                self.books[book_name] = "available"
                self.save_books()
                print(f"You have returned '{book_name}'.")
            else:
                print(f"The book '{book_name}' was not borrowed.")
        else:
            print(f"The book '{book_name}' does not exist in the library.")

    def display_books(self):
        if self.books:
            for book, status in self.books.items():
                print(f"{book}: {status}")
        else:
            print("The library is empty.")

def main():
    library = Library("books.json")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '2':
            book_name = input("Enter the name of the book to remove: ")
            library.remove_book(book_name)
        elif choice == '3':
            book_name = input("Enter the name of the book to borrow: ")
            library.borrow_book(book_name)
        elif choice == '4':
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
        elif choice == '5':
            library.display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()