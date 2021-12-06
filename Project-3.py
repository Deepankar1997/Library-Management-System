class Library:

    def __init__(self, List_of_Books):
        self.Books = List_of_Books

    def Display_Available_Books(self):

        print("Books available in this library are : ")

        for Book in self.Books:
            print(Book)

    def Borrow_Book(self, Bookname):

        if Bookname in self.Books:
            print(
                f"You have been issued the book name - {Bookname}. Kindly please return this book within 30 days.")
            self.Books.remove(Bookname)
            return True

        else:
            print("SORRY! Your requested book is either not available or has already been taken. Kindly please wait till we get back with the book.")
            return False

    def Return_Book(self, Bookname):
        self.Books.append(Bookname)
        print("Thanks for returning this book, hope you have enjoyed it.")

    def Donate_Book(self, Book_To_Donate):
        self.Books.append(Book_To_Donate)
        print("Thank you for your great generosity! We, at Central Library, greatly appreciate your donation.")

    def Library_card_Details(self, name, Contact_Number):
        self.name = name
        self.Contact_Number = Contact_Number


class Student:

    def Request_Book(self):

        self.Books = input("Enter the book name you want to borrow :- ")
        return self.Books

    def Return_Book(self):

        self.Books = input("Enter the book name you want to return :- ")
        return self.Books

    def Donate_Book(self):
        self.Books = input("Enter the book name you want to donate :- ")
        return self.Books

    def Your_Details(self):
        print("Hello Sir/Ma'am !\nFor our Library Membership card, you can apply online as well as ofline.")

        print("\nKindly provide the following details-")

        self.name = input("Please enter your name :- ")
        self.Contact_Number = int(input("Enter your Contact number :-"))
        Greet = '''Congratulations! You have been successfully registered for Library Card. 
Please collect your Library Card from our nearest branch.'''
        print(Greet)


if __name__ == "__main__":
    Central_Library = Library(
        ["Algorithms", "Coding", "C++", "Python", "JAVA", "PHP", "HTML"])
    # Central_Library.Display_Available_Books()  this is to show books before the welcome message and we want to show that
    # this is for borrow book function
    student = Student()


while(True):

    Welcome_Message = '''===== Welcome to Central Library =====
    Please choose the option :-
    1. List of available books.
    2. Request to borrow book.
    3. Return a book.
    4. Doante Book.
    5. Library Membership Card.
    6. Press 6 to exit the program.
    '''
    print(Welcome_Message)

    Choice = int(input("Choose an option from below :- "))
    if (Choice == 1):
        Central_Library.Display_Available_Books()

    elif (Choice == 2):
        Central_Library.Borrow_Book(student.Request_Book())

    elif (Choice == 3):
        Central_Library.Return_Book(student.Return_Book())

    elif (Choice == 4):
        Central_Library.Donate_Book(student.Donate_Book())

    elif (Choice == 5):
        Central_Library.Library_card_Details(student.Your_Details())

    elif (Choice == 6):
        print("Thanks for visiting - The Central Library. Have a great day ahead.")
        exit()

    else:
        print("You have entered an invalid input!")
