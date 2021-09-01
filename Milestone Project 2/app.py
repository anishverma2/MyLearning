from utils import databases_csv as cv
from utils import databases_json as js
from utils import databases_sqlite as db

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """

def menu():
    db.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            prompt_list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Wrong Input Entered!!! \nPlease enter again")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name, author = input("Enter the name and author of the book: ").split()
    db.add_book(name, author)

def prompt_list_books():
    books = db.list_books()
    for book in books:
        print(book)

def prompt_read_book():
    name = input("Enter the name of the book: ")
    db.mark_read_book(name)

def prompt_delete_book():
    name = input("Enter the name of the book: ")
    db.delete_book(name)


if __name__ == '__main__':
    user = input("Please let us know whether you want to store the books in csv or json or database(db) file: ")
    if user == 'csv':
        db = cv
    elif user == 'json':
        db = js
    elif user == 'db':
        db = db
    else:
        print("Wrong input entered!!! Exiting !!!")
        exit()
    menu()
