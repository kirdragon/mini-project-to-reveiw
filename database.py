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
                            year INTEGER,
                            status BOOLEAN
                            )""")
        self.connection.commit()
        
    def add_book(self,book):
        self.cursor.execute("""
                            INSERT INTO books(name,author, year, status)
                            VALUES(?, ?, ?, ?)""",(book.name, book.author, book.year, book.status))
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
    
    def change_status(self, choice, index):
            self.cursor.execute("""
                                UPDATE books
                                SET status = ?
                                WHERE id = ?
                                """,(choice, index))
            self.connection.commit()
    
    def get_id(self,ind):
        self.cursor.execute("""
                            SELECT 1 FROM books
                            WHERE id = ?
                            """,(ind,))
        return self.cursor.fetchone()
    def close(self):
        self.cursor.close()
        self.connection.close()