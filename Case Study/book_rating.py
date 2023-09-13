
from dataclasses import dataclass


@dataclass
class BookRating():
    """
    Represents a book rating system.

    Attributes:
        book_ratings (dict): A dictionary to store book ratings with ISBN as keys and a list of ratings as values.
    """

    def __init__(self, serial_no, isbn,  rating=[]):
        self.serial_no = serial_no
        self.isbn = isbn
        self.rating = rating
