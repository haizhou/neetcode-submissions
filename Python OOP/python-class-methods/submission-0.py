class Library:
    books_available = 100    # Total books in library

    # TODO: Implement class methods to manage book lending
    @classmethod
    def lend_books(cls, lend_num: int) -> None:
        Library.books_available -= lend_num
    # TODO: Implement return_books method to increase the number of books available

    @classmethod
    def return_books(cls, return_books: int) -> None:
        Library.books_available += return_books


# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
