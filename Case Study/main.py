""" 
Books: 
 - ISBN (unique for every Book) - Int
 - Title - string
 - Author - string
 - Year of Publication - Date(Y)
 - Publisher - String 
 - Image URL S - Weblink/Text
 - Image URL M - Weblink/Text
 - Image URL L - Weblink/Text
 
Books-Rating:
 - Serial No(unique for every book rating) - Int
 - ISBN (Unique for every book) - Int 
 - Rating - list of float
 
Users:
 - Serial No - Int 
 - Address - text
 - Area Code - Int
 
 
Create a python application to handle the following. 
Create constructors 
 - Three constructors for each class to define their own specific variables

add_book() to add a new book --Done
- Parameters would be ISBN, Title, Author, YOP, Publisher, Image URL's S,M and L

Del_book() to delete a book --Done
- deleting ISBN would delete all the data related to that book

Update_book() to update book name --Done
- Take book's ISBN and change the Book Title 

Check_title() to check availability of a book by title --Done
- Check the dict by user.title == book.title

Check_isbn() to check availability of a book by isbn  --Done
- check the dict by user.ISBN == Book.isbn

Add_user() to add new user --Done
- Add user to User class with atributes such as Serial No, Address and Area code

Change_user() to update user details --Done
- Update user to update the details of the user in users class

Issue() to issue book to user --Done
- Verify the user is registered 
- Check the availabiliy of the book 
- 

Return_book() to return the book , also calculate the late fee. --Done 
		Book is issued for 7 days. Late fee is applied if returned after 7 days, rs 10 		per day.
- add_rating() to add rating of a book by a user. --Done
 Display() to display ISBN, area code and rating of books
Avg_rating() to calculate the average ratings of books per publisher. --Done
Total() to calculate total number of books published every year.
Top_five() to display five most popular books -- Done

Note :
Use classes to implement the application
Use composition and inheritance , where applicable 
Use List/dictionary as required.
"""

from library import Library
from datetime import date, datetime

# Add books to the Library
# Sample book data
books_data = [
    {
        "isbn": 9518,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year_of_publication": datetime(1960, 7, 11),
        "publisher": "J. B. Lippincott & Co.",
        "image_url_s": "url_s1",
        "image_url_m": "url_m1",
        "image_url_l": "url_l1"
    },
    {
        "isbn": 5007,
        "title": "The Help",
        "author": "Kathryn Stockett",
        "year_of_publication": datetime(2009, 2, 10),
        "publisher": "Penguin Books",
        "image_url_s": "url_s2",
        "image_url_m": "url_m2",
        "image_url_l": "url_l2"
    },
    {
        "isbn": 1284,
        "title": "Eat, Pray, Love",
        "author": "Elizabeth Gilbert",
        "year_of_publication": datetime(2006, 2, 16),
        "publisher": "Viking Press",
        "image_url_s": "url_s3",
        "image_url_m": "url_m3",
        "image_url_l": "url_l3"
    },
    {
        "isbn": 9090,
        "title": "Where the Crawdads Sing",
        "author": "Delia Owens",
        "year_of_publication": datetime(2018, 8, 14),
        "publisher": "G.P. Putnam's Sons",
        "image_url_s": "url_s4",
        "image_url_m": "url_m4",
        "image_url_l": "url_l4"
    },
    {
        "isbn": 5009,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year_of_publication": datetime(1925, 4, 10),
        "publisher": "Scribner",
        "image_url_s": "url_s5",
        "image_url_m": "url_m5",
        "image_url_l": "url_l5"
    },
    {
        "isbn": 6023,
        "title": "The Girl on the Train",
        "author": "Paula Hawkins",
        "year_of_publication": datetime(2015, 1, 13),
        "publisher": "Riverhead Books",
        "image_url_s": "url_s6",
        "image_url_m": "url_m6",
        "image_url_l": "url_l6"
    },
    {
        "isbn": 8498,
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "year_of_publication": datetime(2019, 2, 5),
        "publisher": "Celadon Books",
        "image_url_s": "url_s7",
        "image_url_m": "url_m7",
        "image_url_l": "url_l7"
    },
    {
        "isbn": 5530,
        "title": "All the Light We Cannot See",
        "author": "Anthony Doerr",
        "year_of_publication": datetime(2014, 5, 6),
        "publisher": "Scribner",
        "image_url_s": "url_s8",
        "image_url_m": "url_m8",
        "image_url_l": "url_l8"
    },
    {
        "isbn": 7753,
        "title": "The Goldfinch",
        "author": "Donna Tartt",
        "year_of_publication": datetime(2013, 10, 22),
        "publisher": "Little, Brown and Company",
        "image_url_s": "url_s9",
        "image_url_m": "url_m9",
        "image_url_l": "url_l9"
    },
    {
        "isbn": 2415,
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "year_of_publication": datetime(2003, 3, 18),
        "publisher": "Doubleday",
        "image_url_s": "url_s10",
        "image_url_m": "url_m10",
        "image_url_l": "url_l10"
    },
]

# Sample user data
users_data = [
    {"serial_no": 1, "address": "Address1", "area_code": 1001},
    {"serial_no": 2, "address": "Address2", "area_code": 1002},
    {"serial_no": 3, "address": "Address3", "area_code": 1003},
    {"serial_no": 4, "address": "Address4", "area_code": 1004},
    {"serial_no": 5, "address": "Address5", "area_code": 1005},
    {"serial_no": 6, "address": "Address6", "area_code": 1006},

]

# Sample book ratings data
book_ratings_data = [
    {"serial_no": 1, "isbn": 9518, "rating": 4.5},
    {"serial_no": 2, "isbn": 9518, "rating": 3.0},
    {"serial_no": 5, "isbn": 9518, "rating": 4.5},
    {"serial_no": 4, "isbn": 2415, "rating": 3.0},
    {"serial_no": 5, "isbn": 7753, "rating": 4.5},
    {"serial_no": 3, "isbn": 2415, "rating": 3.0},
    {"serial_no": 4, "isbn": 8498, "rating": 4.5},
    {"serial_no": 1, "isbn": 7753, "rating": 3.0},
    {"serial_no": 1, "isbn": 2415, "rating": 4.5},
    {"serial_no": 4, "isbn": 9090, "rating": 3.0},
    {"serial_no": 5, "isbn": 5007, "rating": 4.5},
    {"serial_no": 3, "isbn": 7753, "rating": 3.0},
    {"serial_no": 2, "isbn": 7753, "rating": 4.5},
    {"serial_no": 2, "isbn": 9090, "rating": 3.0},
    {"serial_no": 2, "isbn": 6023, "rating": 3.0},
    {"serial_no": 1, "isbn": 5007, "rating": 4.5},
    {"serial_no": 4, "isbn": 7753, "rating": 3.0},
    {"serial_no": 1, "isbn": 5007, "rating": 4.5},
    {"serial_no": 5, "isbn": 2415, "rating": 3.0},
    {"serial_no": 3, "isbn": 5007, "rating": 3.0},
    {"serial_no": 3, "isbn": 8498, "rating": 4.5},
    {"serial_no": 2, "isbn": 5007, "rating": 3.0},
    {"serial_no": 1, "isbn": 8498, "rating": 4.5},
    {"serial_no": 2, "isbn": 8498, "rating": 3.0}
]

# Example usage:
for book_data in books_data:
    Library.add_book(**book_data)

for user_data in users_data:
    Library.add_user(**user_data)

for rating_data in book_ratings_data:
    Library.add_rating(**rating_data)

print("\n\n\n\n")
print("-" * 180)
print("\n\n\t\t\t\t\t\t\t\t\tMain Menu for Library Management System\n\n")
print("-" * 180)

print("\n\n1. Add Book to the System")
print("\n2. Delete book from the System")
print("\n3. Update exisiting book in the System")
print("\n4. Check availability of the book from the System using Book Title")
print("\n5. Check availability of the book from the System using Book ISBN")
print("\n6. Add user in the Library")
print("\n7. Update/Change user in the Library")
print("\n8. Issue a book to the user")
print("\n9. Book returns")
print("\n10. Add user rating for a book")
print("\n11. Display book details in the system")
print("\n12. Get the avg rating of books per publisher")
print("\n13. Get total number of book published by year")
print("\n14. Get the top 5 books based on Avg rating")
print("\n15. Quit")

while True:
    menu_item = int(
        input("\n\n\nEnter the action you would like to perform: "))
    f = 0
    match menu_item:
        case 1:
            # User book addition
            while True:
                print(
                    "\nEnter the details of the book you want to add or enter exit to Quit\n")
                add_book_isbn = input("\nEnter the ISBN for the book: ")
                if (str(add_book_isbn) in ["Exit", "exit"]):
                    break
                elif (add_book_isbn != "" and int(add_book_isbn) > 0 and int(add_book_isbn) not in Library.books):
                    add_book_title = input(
                        "\nEnter the Title for the book: ")
                    add_book_author = input(
                        "\nEnter the Author for the book: ")
                    add_book_year_of_publication = int(
                        input("\nEnter the Year of Publication for the book: "))
                    add_book_month_of_publication = int(
                        input("\nEnter the Month of Publication for the book: "))
                    add_book_date_of_publication = int(
                        input("\nEnter the Date of Publication for the book: "))
                    add_book_publisher = input(
                        "\nEnter the Publisher for the book: ")
                    add_book_image_url_s = input(
                        "\nEnter the Small URL for the book: ")
                    add_book_image_url_m = input(
                        "\nEnter the Medium URL for the book: ")
                    add_book_image_url_l = input(
                        "\nEnter the Long URl for the book: ")

                    Library.add_book(
                        int(add_book_isbn),
                        add_book_title,
                        add_book_author,
                        date(add_book_year_of_publication,
                             add_book_month_of_publication, add_book_date_of_publication),
                        add_book_publisher,
                        add_book_image_url_s,
                        add_book_image_url_m,
                        add_book_image_url_l
                    )

        case 2:
            Library.del_book()

        case 3:
            Library.update_book()

        case 4:
            Library.check_title()

        case 5:
            while True:
                user_isbn = input(
                    "\n\nEnter the ISBN of the book you would like to search in the system: ")
                if (user_isbn in ["Exit", "exit"]):
                    break

                elif (int(user_isbn) > 0 and user_isbn != ""):
                    if (Library.check_isbn(int(user_isbn))):
                        print(
                            f"\n\nBook with ISBN '{user_isbn}' found in the System.")
                    else:
                        print(
                            f"\n\nBook with ISBN '{user_isbn}' not found in the System.")
                else:
                    print("\n\nNot a valid ISBN")

        case 6:
            user_serial_no = input("\n\nEnter the serial number of the user: ")
            user_address = input(
                "\n\nEnter the user address of the new user: ")
            user_area_code = input("\n\nEnter the area code of the new user: ")

            Library.add_user(user_serial_no, user_address, user_area_code)

        case 7:
            user_new_serial_no = input(
                "\n\nEnter the serial no of the user you want to update: ")
            user_new_address = input("\n\nEnter the new address of the user: ")
            user_new_area_code = input(
                "\n\nEnter the new area code of the user: ")

            Library.change_user(user_new_serial_no,
                                user_new_address, user_new_area_code)

        case 8:
            user_issue_serial_no = input(
                "\n\nEnter the serial number of the User you want to issue the book to: ")
            user_issue_book_isbn = input(
                "\n\nEnter the book isbn to issue to the user: ")
            Library.issue(user_issue_serial_no, user_issue_book_isbn)

        case 9:
            user_return_serial_no = input(
                "\n\nEnter the serial no of the user: ")
            user_return_book_isbn = input(
                "\n\nEnter the ISBN of the book the user wants to return: ")
            Library.return_book(user_return_serial_no, user_return_book_isbn)

        case 10:
            user_rating_serial_no = input("\n\nEnter serial no: ")
            user_rating_isbn = input("\n\nEnter ISBN for the book: ")
            user_new_rating = input("\n\nEnter the rating for the book: ")

            Library.add_rating(user_rating_serial_no,
                               user_rating_isbn, user_new_rating)

            print(
                f"\n\nUser rating for the book with ISBN '{user_rating_isbn}' updated")

        case 11:
            Library.display()

        case 12:
            Library.avg_rating()

        case 13:
            Library.total()
        case 14:
            Library.top_five()
        case 15:
            print("\n You have successfully exited the application")
            break

        case default:
            print("\n\nEnter a option 1 - 15")
