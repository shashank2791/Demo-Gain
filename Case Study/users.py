from dataclasses import dataclass


@dataclass
class Users:
    """
    Represents a collection of library users.
    """

    def __init__(self, serial_no, address, area_code):

        self.serial_no = serial_no
        self.address = address
        self.area_code = area_code

    def __str__(self):
        return f"Serial No: {self.serial_no}, Address: {self.address}, Area Code: {self.area_code}"
