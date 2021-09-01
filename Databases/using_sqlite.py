import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
'''
all operations in sqlite are made by cursor, and not by the connection object itself
with multiple cursor we can perform different read operations at a time
in sqlite we can perform only one write operation at once however we can perform many read operations simultaneously
it has been called as cursor because the cursor point to the current position and goes to the next row as we will tell and cannot come back to previous row
'''
cursor.execute("create table anish (name varchar2);")
cursor.execute("Insert into anish values('Verma')")
print(cursor.execute("Select * from anish"))

connection.commit()     #it just mean save the result to the disk

connection.close()