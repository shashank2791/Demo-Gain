from dataclasses import dataclass
from book_rating import BookRating


@dataclass
class Book(BookRating):
    def __init__(self, isbn, title, author, year_of_publication, publisher, image_url_s, image_url_m, image_url_l):
        """
        Initialize a Book object with the provided attributes.

        Args:
            isbn (int): The ISBN (unique identifier) of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            year_of_publication (date): The year of publication of the book.
            publisher (str): The publisher of the book.
            image_url_s (str): The URL for the small-sized book image.
            image_url_m (str): The URL for the medium-sized book image.
            image_url_l (str): The URL for the large-sized book image.


        Attributes:
            isbn (int): The ISBN of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            year_of_publication (date): The year of publication of the book.
            publisher (str): The publisher of the book.
            image_url_s (str): The URL for the small-sized book image.
            image_url_m (str): The URL for the medium-sized book image.
            image_url_l (str): The URL for the large-sized book image.
            ratings (list of float): List of ratings given to the book.

        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        self.img_url_s = image_url_s
        self.img_url_m = image_url_m
        self.img_url_l = image_url_l
        self.ratings = []
        # self.issued_to = None
        # self.due_date = None

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Year of Publication: {self.year_of_publication}, Publisher: {self.publisher}"
