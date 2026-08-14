from book import Book
from database import Database

class Manager:
    def __init__(self):
        self.database = Database()
        
    def add_book(self, name, author, year, status):
        book = Book(name,author, year,status)
        self.database.add_book(book)
        
    def delete_book(self, index):
        self.database.delete_book(index)
    
    def get_books(self):
        return self.database.show_books()
    
    def change_status(self, choice, index):
        self.database.change_status(choice, index)
    
    def check_id(self,ind):
            if self.database.get_id(ind):
                return self.database.get_id(ind)
            else:
                print("Please enter an existing ID!")
                