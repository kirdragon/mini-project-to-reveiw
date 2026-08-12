import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("books.db")
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS books(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            author TEXT,
                            status BOOLEAN,
                            year INREGER
                            )""")
        self.connection.commit()
        
    def add_book(self,book):
        self.cursor.execute("""
                            INSERT INTO books(name,author,status, year)
                            VALUES(?, ?, ?, ?)""",(book.name, book.author, book.status, book.year))
        self.connection.commit()
    
    def delete_book(self,index):
        self.cursor.execute("""
                            DELETE FROM books
                            WHERE id = ?;
                            """,(index,))
        self.connection.commit()
    
    def show_books(self):
        self.cursor.execute("""
                            SELECT * FROM books;
                            """)
        rows = self.cursor.fetchall()
        
        return(rows)
    
    def close(self):
        self.cursor.close()