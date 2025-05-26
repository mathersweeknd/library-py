class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")

    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'Book "{title}" removed from the library.')
                return
        print(f'No book found with the title "{title}".')


def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Remove Book")
    print("5. Exit")


def main():
    library = Library()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year of publication: ")
            book = Book(title, author, year)
            library.add_book(book)
        
        elif choice == '2':
            library.list_books()
        
        elif choice == '3':
            query = input("Enter title or author to search: ")
            library.search_books(query)
        
        elif choice == '4':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        
        elif choice == '5':
            print("Exiting the library management system.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()