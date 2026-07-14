import json
class Student:

    def __init__(self, first_name, last_name, regno, program,  email):
        self.first_name = first_name
        self.last_name = last_name
        self.regno = regno
        self.program = program
        self.email = email

    def show(self):
        print("----------------")
        print("First Name :", self.first_name)
        print("Last name:", self.last_name)
        print("Register no:", self.regno)
        print("Program: ", self.program)
        print("Email:", self.email)
        print("----------------")

students = []
def save_students():

    data = []

    for s in students:

        student = {
            "first_name": s.first_name,
            "last_name": s.last_name,
            "regno": s.regno,
            "program": s.program,
            "email": s.email
        }

        data.append(student)

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

def load_students():

    global students

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            for student in data:

                new_student = Student(
                    student["first_name"],
                    student["last_name"],
                    student["regno"],
                    student["program"],
                    student["email"]
                )

                students.append(new_student)

    except FileNotFoundError:
        pass

def dashboard1():
    print("\n======Student Management System======\n")


def welcome1():
    print("Press 1 to Add Student")
    print("Press 2 to Remove Student")
    print("Press 3 to Show Studnet")
    print("Press 4 to Search Student")
    print("Press 5 to Update Student")
    print("Press 0 to Exit!")


def add_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    regno = input("Enter Register no: ")
    program = input("Enter Program: ")
    email = input("Enter email: ")

    new_student = Student(first_name, last_name , regno, program, email)
    for s in students:
        if s.regno.lower() == regno.lower():
            print("Registration number already exists!")
            return
    students.append(new_student)
    save_students()

    print("Student added successfully")


def show_student():
    if not students:
        print("No student found")
    else:
        for s in students:     
            s.show()


def search_student():
    number = input("\nEnter the register number you want to search: ")

    found = False

    for s in students:
        if number.lower() == s.regno.lower():
            print("\nStudent Found!")
            s.show()
            found = True
            break

    if not found:
        print("Student not found!")


def remove_student():
    number = input("\nEnter the register number you want to delete: ")

    found = False

    for s in students:
        if number.lower() == s.regno.lower():
            s.show()
            students.remove(s)
            save_students()
            print("\nStudent Removed.")
            found = True
            break

    if not found:
        print("Student not found!")

def update_student():
    number = input("\nEnter the registration number to update: ")

    found = False

    for s in students:
        if number.lower() == s.regno.lower():

            print("\nCurrent Student Details:")
            s.show()

            print("\nEnter New Details")

            s.first_name = input("First Name: ")
            s.last_name = input("Last Name: ")
            s.program = input("Program: ")
            s.email = input("Email: ")
            save_students()
            print("\nStudent updated successfully!")
            

            found = True
            break

    if not found:
        print("Student not found!")

choices = [0, 1, 2, 3, 4, 5]


def student_menu():

    while True:

        dashboard1()
        welcome1()

        try:
            choice = int(input("Press Any number: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if choice not in choices:
            print("Invalid choice!\n")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            remove_student()

        elif choice == 3:
            show_student()

        elif choice == 4:
            search_student()

        elif choice == 5:
            update_student()

        elif choice == 0:
            print("Thankyou!")
            break
        
class Book:

    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

    def show(self):
        print("----------------")
        print("Title :", self.title)
        print("Author:", self.author)
        print("Availability:", self.availability)
        print("----------------")

books = []
def save_books():

    books_data = []

    for b in books:

        book = {
            "title": b.title,
            "author": b.author,
            "availability": b.availability,

        }

        books_data.append(book)

    with open("books.json", "w") as file:
        json.dump(books_data, file, indent=4)

def load_books():

    global books

    try:
        with open("books.json", "r") as file:
            data = json.load(file)

            for book in data:

                new_book = Book(
                    book["title"],
                    book["author"],
                    book["availability"]
                )

                books.append(new_book)

    except FileNotFoundError:
        pass

def dashboard2():
    print("\n======Books Management======\n")


def welcome2():
    print("Press 1 to Add Book")
    print("Press 2 to Remove Book")
    print("Press 3 to Show Book")
    print("Press 4 to Search Book")
    print("Press 5 to Update Book")
    print("Press 0 to Exit!")


def add_book():
    title = input("Title: ")
    author = input("Author: ")
    while True:
        try:
            availability = int(input("Availability: "))

            if availability < 0:
                print("Availability cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    new_book = Book(title, author, availability)
    for b in books:
        if b.title.lower() == title.lower():
            print("Book already exists!")
            return
    books.append(new_book)
    save_books()
    print("\nBook added successfully\n")


def show_book():
    if not books:
        print("No book found")
    else:
        for b in books:     
            b.show()


def search_book():
    title = input("Enter title: ")

    found = False

    for b in books:
        if title.lower() == b.title.lower():
            print("\nBook Found!")
            b.show()
            found = True
            break

    if not found:
        print("Book not found!")


def remove_book():
    title = input("Enter title: ")

    found = False

    for b in books:
        if title.lower() == b.title.lower():
            b.show()
            books.remove(b)
            save_books()
            print("\nBook Removed.")
            found = True
            break

    if not found:
        print("Book not found!")

def update_book():
    title = input("Enter title to update: ")

    found = False

    for b in books:
        if title.lower() == b.title.lower():

            print("\nCurrent Book Details:")
            b.show()

            print("\nEnter New Details")

            b.title = input("Title: ")
            b.author = input("Author: ")
            while True:
                try:
                    b.availability = int(input("Quantity: "))

                    if b.availability < 0:
                        print("Quantity cannot be negative.")
                        continue
                

                    break

                except ValueError:
                    print("Please enter a valid number.")
            save_books()

            print("\nBook updated successfully!")

            found = True
            break

    if not found:
        print("Book not found!")

choices = [0, 1, 2, 3, 4, 5]


def book_menu():

    while True:

        dashboard2()
        welcome2()

        try:
            choice = int(input("Press Any number: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if choice not in choices:
            print("Invalid choice!\n")
            continue

        if choice == 1:
            add_book()

        elif choice == 2:
            remove_book()

        elif choice == 3:
            show_book()

        elif choice == 4:
            search_book()

        elif choice == 5:
            update_book()

        elif choice == 0:
            print("Thankyou!")
            break
        
def dashboard3():
    print("\n======Borrowed/Returned Books Info======\n")

def welcome3():
    print("Press 1 to borrow book")
    print("Press 2 to return book")
    print("Press 3 to show all books info")
    print("Press 0 to Exit!")

class BorrowRecord():
    def __init__(self, student, title, quantity):
        self.student = student
        self.title = title
        self.quantity = quantity

    def show(self):
        print("-----------------------------")
        print("Student: ", self.student)
        print("Book Title: ", self.title)
        print("Quantity: ", self.quantity)
        print("-----------------------------")
    
borrowed = []
def save_borrowed():

    borrowed_data = []

    for borrow in borrowed:

        borrows = {
            "student": borrow.student,
            "title": borrow.title,
            "quantity": borrow.quantity,
        }

        borrowed_data.append(borrows)

    with open("library.json", "w") as file:
        json.dump(borrowed_data, file, indent=4)

def load_borrowed():

    global borrowed

    try:
        with open("library.json", "r") as file:
            data = json.load(file)

            for record in data:

                new_record = BorrowRecord(
                    record["student"],
                    record["title"],
                    record["quantity"]
                )

                borrowed.append(new_record)

    except FileNotFoundError:
        pass

def borrow_books():

    regno = input("Enter Student Registration Number: ")
    title = input("Enter Book Title: ")
    while True:
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
                        
            break

        except ValueError:
            print("Please enter a valid quantity.")
    student_found = None
    book_found = None

    # Search student
    for s in students:
        if s.regno.lower() == regno.lower():
            student_found = s
            break

    if student_found is None:
        print("Student not found!")
        return

    # Search book
    for b in books:
        if b.title.lower() == title.lower():
            book_found = b
            break

    if book_found is None:
        print("Book not found!")
        return

    # Check availability
    if quantity > book_found.availability:
        print("Not enough books available!")
        return

    # Reduce available quantity
    book_found.availability -= quantity

    # Save borrow record
    record = BorrowRecord(
    student_found.regno,
    book_found.title,
    quantity
)

    borrowed.append(record)
    save_borrowed()
    save_books()      
    print("Book borrowed successfully!")

def return_books():

    regno = input("Enter Student Registration Number: ")
    title = input("Enter Book Title: ")

    found = False

    for record in borrowed:

        if (record.student.lower() == regno.lower() and record.title.lower() == title.lower()):

                # Increase availability again
            for b in books:
                if b.title == title:
                    b.availability += record.quantity
                    break

            borrowed.remove(record)
            save_borrowed()
            save_books()

            print("Book returned successfully!")

            found = True
            break

    if not found:
        print("Borrow record not found!")

def show_book_summary():
    if not borrowed:
        print("Nothing Borrowed yet!")
    else:
        for b in borrowed:
            b.show()


choices = [0,1,2,3]

def borrowed_menu():

    while True:

        dashboard3()
        welcome3()

        try:
            choice = int(input("Press Any number: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if choice not in choices:
            print("Invalid choice!\n")
            continue

        if choice == 1:
            borrow_books()

        elif choice == 2:
            return_books()

        elif choice == 3:
            show_book_summary()

        elif choice == 0:
            print("Thankyou!")
            break


def dashboard():
    print("\n======Library Management System======\n")

def welcome():
    print("Press 1 to open Students portal")
    print("Press 2 to open book store")
    print("Press 3 to borro/return books")
    print("Press 0 to Exit!")


def main_menu():

    while True:

        dashboard()
        welcome()

        try:
            choice = int(input("Press Any number: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if choice not in choices:
            print("Invalid choice!\n")
            continue

        if choice == 1:
            student_menu()

        elif choice == 2:
            book_menu()

        elif choice == 3:
            borrowed_menu()

        elif choice == 0:
            print("Thankyou!")
            break

load_students()
load_books()
load_borrowed()   
main_menu()