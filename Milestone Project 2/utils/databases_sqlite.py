from typing import List, Dict, Union
from .database_connection import DatabaseConnection

'''
Concerned with storing and retriving books from database
'''
book = Dict[str, Union[str, int]]
books_file = 'data.db'

def create_book_table() -> None: #this is type hinting in python which we can use only in pychar which tells us whenever we call this function and try to assign its value to anything that its returns nothing
    # database connection example as context manager
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('Create table books(name text primary key, author text, read integer)')
    '''
    using the database connection normally
    connection = sqlite3.connect(books_file)
    cursor = connection.cursor()
    
    SQLITE only supports only 5 types of data namely: NULL, INTEGER, REAL(floating number), TEXT, BLOB(binary data field to store images, pdf and other stuff)
    
    cursor.execute('Create table books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()'''

def add_book(name: str, author: str) -> None:   #we can also use type hinting for parameters which tells us that what type of data a fun is expectin and can give warnin if there is a data typs mismatch
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        #below statement is not recommended in dqlite execute because of the f string, so we will do another approach. It causes sql injection attack
        #cursor.execute(f'Insert into books values("{name}", "{author}", 0)') #giving double quotes so that sqlite should know that we are giving strings
        cursor.execute('Insert into books values(?, ?, 0)', (name, author)) #sqlite automatically puts the value of name and author in the place specified by ? order wise


def list_books() -> List[book]: # for list and dict we need to import the required module which tells which type it belongs to the calling side
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()

        cursor.execute('Select * from books')
        #books = cursor.fetchall()   #fetch all the rows of the books table, gives list of tuples [(name , author read), (name, author, read)]
        #instead of above statement we can do a dictionary comprehension to have all the details in the same format as we want

        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books

def mark_read_book(name) -> None:   #we can use this type hinting only in pycharm as pychar only supports it for efficient coding
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()

        cursor.execute('Update books set read=1 where name = ?', (name,))   #we should always give the values as tuple or else it will execute it as arguments


def delete_book(name) -> None:
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()

        cursor.execute('Delete from books where name = ?', (name,))
