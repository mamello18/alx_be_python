from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("1984", "George Orwell", 1949)
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 1992, 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

    # Example of __repr__ usage
    print(repr(classic_book))

    # Example of deleting a book
    print(f"Deleting {classic_book.title}")
    my_library.books.remove(classic_book)

    # List remaining books
    my_library.list_books()

if __name__ == "__main__":
    main()
