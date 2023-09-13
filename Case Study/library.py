from datetime import timedelta, date
from books import Book
from users import Users


class Library:
    """
    Represents a library management system.

    Attributes:
        books (dict): A dictionary to store Book objects with ISBN as keys.
        users (dict): A dictionary to store User objects with serial numbers as keys.
    """
    books = {}
    users = {}

    @staticmethod
    def add_book(isbn, title, author, year_of_publication, publisher, image_url_s, image_url_m, image_url_l):
        """
        Add a new book to the library's collection.

        Args:
            isbn (int): The ISBN of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            year_of_publication (date): The year of publication of the book.
            publisher (str): The publisher of the book.
            image_url_s (str): The URL for the small-sized book image.
            image_url_m (str): The URL for the medium-sized book image.
            image_url_l (str): The URL for the large-sized book image.

        Raises:
            Exception: Exception name
        """
        try:
            isbn = int(isbn)
            if isbn <= 0 or isbn == "":
                print("\n\nISBN must be a positive integer and non-empty")
            else:
                if isbn in Library.books:
                    print(f"\n\nBook with ISBN {isbn} already exists.")

                else:
                    book = Book(isbn, title, author, year_of_publication,
                                publisher, image_url_s, image_url_m, image_url_l)
                    Library.books[isbn] = book
                    if isbn in Library.books:
                        print(
                            f"\n\nBook '{book.title}' added successfully to the System.")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def del_book():
        """
        Delete a book from the library's collection.

        Raises:
            Exception: Exception name
        """
        try:
            while True:
                del_book_isbn = input(
                    "\n\nEnter the ISBN of the book you want to delete or enter exit to Quit: ")
                if (str(del_book_isbn) in ["Exit", "exit"]):
                    break
                elif (del_book_isbn != "" and int(del_book_isbn) in Library.books):
                    del Library.books[int(del_book_isbn)]
                    print('\n\nBook with ISBN "' + str(del_book_isbn) +
                          '" deleted from the system successfully.\n')
                else:
                    print('\n\nBook with ISBN "' + str(del_book_isbn) +
                          '" not found in the system or please enter a valid ISBN\n')

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def update_book():
        """
        Update the title of a book in the library's collection.

        Raises:
            Exception: Exception name
        """
        try:
            while True:
                isbn = input(
                    "\n\nEnter the ISBN of the book you want to modify or enter exit to quit: ")
                if (isbn in ["Exit", "exit"]):
                    break
                elif int(isbn) <= 0:
                    print("\n\nISBN must be a positive integer.")

                elif int(isbn) in Library.books:
                    isbn = int(isbn)
                    print(
                        f"\n\nThe current book name for ISBN '{isbn}' is '{Library.books[isbn].title}'")
                    new_title = input("\n\nEnter the new title of the book: ")
                    if not new_title:
                        print("\n\nNew title cannot be empty.")

                    Library.books[isbn].title = new_title
                    print(
                        f"\n\nBook title updated to '{new_title}' for ISBN {isbn}.")
                else:
                    print(
                        f"\n\nBook with ISBN '{isbn}' not found in the System")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def check_title():
        """
        Check the availability of a book by title.

        Raises:
            Exception: Exception name
        """
        try:
            while True:
                user_title = input(
                    "\n\nEnter the title of the book you want to search or enter exit to Quit: ")
                if (user_title in ["Exit", "exit"]):
                    break
                else:
                    matching_books = [
                        book for book in Library.books.values() if book.title == user_title]
                    if not matching_books:
                        print(
                            f"\n\nBook with title '{user_title}' not found in the System.")
                    else:
                        print(
                            f"\n\nBook with title '{user_title}' found in the System")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def check_isbn(isbn):
        """
        Check the availability of a book by ISBN.

        Args:
            isbn (int): The ISBN of the book to check.

        Returns:
            Book or None: The Book object with the matching ISBN or None if not found.
        """
        return Library.books.get(isbn)

    @staticmethod
    def issue(user_serial_no, book_isbn):
        """
        Issue a book to a user from the library's collection.

        Args:
            user_serial_no (int): The serial number of the user.
            book_isbn (int): The ISBN of the book to be issued.

        Raises:
            Exception: Exception name
        """
        try:
            user_serial_no = int(user_serial_no)
            book_isbn = int(book_isbn)
            if user_serial_no <= 0 or book_isbn <= 0:
                print(
                    "\n\nSerial No and ISBN must be positive integers.")
            else:
                user = Library.users.get(user_serial_no)
                book = Library.books.get(book_isbn)
                if not user:
                    print(
                        f"\n\nUser with Serial No '{user_serial_no}' not found.")
                if not book:
                    print(f"\n\nBook with ISBN '{book_isbn}' not found.")

                if hasattr(book, 'issued_to') and hasattr(book, 'due_date'):
                    print(f"\n\nBook '{book.title}' is already issued.")
                else:
                    due_date = date.today() + timedelta(days=7)
                    book.issued_to = user_serial_no
                    book.due_date = due_date
                    print(
                        f"\n\nBook '{book.title}' is issued to User '{user_serial_no}'. Due on '{due_date}'")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def return_book(user_serial_no, book_isbn):
        """
        Return a book to the library and calculate late fees if applicable.

        Args:
            user_serial_no (int): The serial number of the user returning the book.
            book_isbn (int): The ISBN of the book to be returned.

         Raises:
            Exception: Exception name
        """
        try:
            user_serial_no = int(user_serial_no)
            book_isbn = int(book_isbn)
            if user_serial_no <= 0 or book_isbn <= 0:
                print("\n\nSerial No and ISBN must be positive integers.")

            else:
                user = Library.users.get(user_serial_no)
                book = Library.books.get(book_isbn)

                if not user:
                    print(
                        f"\n\nUser with Serial No '{user_serial_no}' not found.")
                elif not book:
                    print(f"\n\nBook with ISBN '{book_isbn}' not found.")

                elif not hasattr(book, 'issued_to') or not hasattr(book, 'due_date'):
                    print(f"\n\nBook '{book.title}' is not currently issued.")
                elif book.issued_to != user_serial_no:
                    print(
                        f"\n\nBook '{book.title}' is not issued to User '{user_serial_no}'.")

                return_date = date.today()
                if hasattr(book, "due_date"):
                    due_date = book.due_date

                    if book and hasattr(book, "due_date") and return_date > due_date:
                        days_late = (return_date - due_date).days
                        late_fee = days_late * 10
                        print(
                            f"\n\nBook '{book.title}' is returned late by {days_late} days. Late fee: Rs {late_fee}")
                    else:
                        print(f"\n\nBook '{book.title}' is returned on time.")

                    del book.issued_to

                    del book.due_date

        except Exception as error:
            print("\n\nAn exception occurred:", error)

    @staticmethod
    def display():
        """
        Display ISBN, area code, and ratings of books in the library's collection.
        """
        for isbn, book in Library.books.items():
            print(
                f"ISBN: {isbn}, Area Code: {book.publisher}, Ratings: {book.ratings}")

    @staticmethod
    def total():
        """
        Calculate and display the total number of books published every year.
        """
        year_counts = {}

        for book in Library.books.values():
            year = book.year_of_publication.year
            if year not in year_counts:
                year_counts[year] = 0
            year_counts[year] += 1

        for year, count in year_counts.items():
            print(f"Year: {year}, Total Books Published: {count}")

    @staticmethod
    def top_five():
        """
        Display the five most popular books based on the avg rating of books.
        """
        sorted_books = sorted(Library.books.values(),
                              key=lambda book: sum(book.ratings)/len(book.ratings) if book.ratings else 0, reverse=True)
        top_five_books = sorted_books[:5]

        print("Top Five Books:")
        for i, book in enumerate(top_five_books, start=1):
            print(
                f"{i}. Title: {book.title}, ISBN: {book.isbn}, Average Rating: {sum(book.ratings)/len(book.ratings):.2f}")

    @staticmethod
    def add_user(serial_no, address, area_code):
        """
        Add a new user to the collection.

        Args:
            serial_no (int): The serial number (unique identifier) for the user.
            address (str): The address of the user.
            area_code (int): The area code of the user.

        Raises:
            Exception: Exception name
        """
        try:
            serial_no = int(serial_no)
            if serial_no <= 0 or serial_no == "":
                print("\n\nSerial No must be a positive integer.")

            elif serial_no in Library.users:
                print(f"\n\nUser with Serial No '{serial_no}' already exists.")

            else:
                user = Users(serial_no, address, area_code)
                Library.users[serial_no] = user
                if serial_no in Library.users:
                    print(
                        f"\n\nUser with Serial No '{serial_no}' addedd successfully to the system.")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def change_user(serial_no, new_address, new_area_code):
        """
        Update the details of a user.

        Args:
            serial_no (int): The serial number (unique identifier) for the user to be updated.
            new_address (str): The new address for the user.
            new_area_code (int): The new area code for the user.

        Raises:
            Exception: Exception name
        """
        try:
            serial_no = int(serial_no)
            if serial_no <= 0:
                print("\n\nSerial No must be a positive integer.")

            elif serial_no in Library.users:
                if not new_address:
                    print("\n\nNew address cannot be empty.")
                else:
                    user = Library.users[serial_no]
                    user.address = new_address
                    user.area_code = new_area_code

                    print(
                        f"\n\nUser with serial no '{serial_no}' updated in the System")

            else:
                print(
                    f"\n\nUser with serial no '{serial_no}' does not exsist in the System.")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def get_user(serial_no):
        """
        Get user information by serial number.

        Args:
            serial_no (int): The serial number (unique identifier) of the user to retrieve.

        Returns:
            User or None: The User object with the matching serial number, or None if not found.
        """
        return Library.users.get(serial_no)

    @staticmethod
    def list_users():
        """
        Get a list of all users in the collection.

        Returns:
            list: A list of User objects representing all users.
        """
        return list(Library.users.values())

    @staticmethod
    def add_rating(serial_no, isbn, rating):
        """
        Add a rating for a book by a user.

        Args:
            serial_no (int): The serial number of the user giving the rating.
            isbn(int) : ISBN of the book for which the user is adding the rating
            rating (float): The rating to be added.

        Raises:
            Exception: Exception name
        """
        try:
            serial_no = int(serial_no)
            isbn = int(isbn)
            rating = float(rating)
            if serial_no <= 0 or isbn <= 0:
                print(
                    "\n\nSerial No and ISBN must be positive integers.")
            elif rating < 1.0 or rating > 5.0:
                print("\n\nRating must be between 1 and 5.")

            else:
                user = Library.get_user(serial_no)
                book = Library.check_isbn(isbn)
                if not user:
                    print(
                        f"\n\nUser with Serial No '{serial_no}' not found.")
                if not book:
                    print(f"\n\nBook with ISBN '{isbn}' not found.")

                if serial_no not in book.ratings:
                    book.ratings.append(rating)
                    # print(
                    # f"Rating of {rating} added for Book '{book.title}' by User {serial_no}.")

        except Exception as error:
            print("\n\nAn exception occurred:", type(error).__name__)

    @staticmethod
    def avg_rating():
        """
        Calculate and display the average ratings of books per publisher.
        """
        publisher_ratings = {}

        for book in Library.books.values():
            if book.publisher not in publisher_ratings:
                publisher_ratings[book.publisher] = []

            publisher_ratings[book.publisher].extend(book.ratings)

        for publisher, ratings in publisher_ratings.items():
            avg_rating = sum(ratings) / len(ratings) if ratings else 0.0
            print(f"Publisher: {publisher}, Average Rating: {avg_rating:.2f}")
