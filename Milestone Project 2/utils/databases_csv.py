'''
Concerned with storing and retrieving books from list
Storing the data into a file as csv

name,author,read\n
name,author,read\n
name,author,read\n
'''

books_file = 'books.txt'

def create_book_table(): #created this method so that the file gets created and won't give us any error
    with open(books_file, 'a'):
        pass


def add_book(name, author):
    with open(books_file, 'a') as file:     #opening the book in append mode so that whenever we can this method it should point to end of file and add new books to the end
        file.write(f'{name},{author},0\n')    #0 for False and 1 for True

def list_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

def mark_read_book(name):
    books = list_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'

    _save_all_books(books)

def _save_all_books(books):     #underscore in the start tells that we will treat it as a private function and we will not call it outside this file
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(name):
    books = list_books()
    books = [book for book in books if book['name'] != name]

    _save_all_books(books)


'''
def prompt_delete_book(name):
    for book in books:
        if name == book['name']:
            books.remove(book)
            return

    print("Book not found !!! ")
'''
