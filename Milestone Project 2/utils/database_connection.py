import sqlite3
'''
this we are creating a context manager for the sqlite database connection and the close statement
'''

class DatabaseConnection:   #in this we should have 2 dunder methods to use it as a context manager
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb): #excetion type, exception value and exception traceback, the other 3 arguments are respectively, all are None by default when no error orrcurs
        if exc_tb or exc_val or exc_type: #if the 3 attributes has a value(except None) that is and error occured then it will just close connection without commiting
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
