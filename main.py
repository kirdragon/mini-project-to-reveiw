from mini_manager import Manager
manager = Manager()
def menu():
    print("1. Add new book\n"
          "2. Delete a book\n"
          "3. Show library\n"
          "4. Change the status of the book\n"
          "5. Finish the programm\n")

def get_int(message, start, end):
    while True:
        try:
            value = int(input(message))
            if start<=value<=end:
                return value
            print(f"Please enter a number from {start} to {end}")
        except ValueError:
            print("Please enter the integer number! ")
            
def get_integer(message):
    try:
        value = int(input(message))
        return value
    except ValueError:
        print("Please enter the integer number! ")

def check_id(message):
    while True:
        try:
            ind = int(input(message))
            if manager.check_id(ind):
                return ind
            show_library()
            print("Please enter an existing ID!")
        except ValueError:
            print("Please enter the integer number! ")

def show_library():
    rows = manager.get_books()
    print("\nThe library:\n")
    for row in rows:
        if row[4]:
            print(f"id - {row[0]}| name - {row[1]}| author - {row[2]}| year - {row[3]}| status - is read")
        else:
            print(f"id - {row[0]}| name - {row[1]}| author - {row[2]}| year - {row[3]}| status - is unread")
    print("")
print("\nWelcome at this fantastic library project!\n")
while True:
    menu()
    choice = get_int("Enter a choice: ", 1, 5)
    if choice == 1:
        name = str(input("name: "))
        author = str(input("author: "))
        year = get_int("year: ", 0, 2026)
        status = get_int("1 - is read\n"
                        "0 - is unread\n"
                        "status: ", 0, 1)
        manager.add_book(name,author,year, status)
        print("The book is added successfully!\n")
    elif choice == 2:
        show_library()
        value = check_id("index: ")
        manager.delete_book(value)
        print(("The book is deleted successfully!\n"))
            
    elif choice == 3:
        show_library()

    elif choice == 4:
        show_library()
        ind = check_id("id: ")
        cho = get_int("1 - is read\n"
                        "0 - is unread\n"
                        "choice: ", 0, 1)
        manager.change_status(cho, ind)
        print("The status is changed successfully!\n")
    elif choice == 5:
        print("Completion of the programm...")
        break