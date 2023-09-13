
from dataclasses import dataclass


@dataclass
class BookRating():
    """
    Represents a book rating system. With serial no, isbn and rating
    """

    def __init__(self, serial_no, isbn,  rating=[]):
        self.serial_no = serial_no
        self.isbn = isbn
        self.rating = rating
