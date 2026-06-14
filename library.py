#library management system
class Library:
    books = []
    issued_books = []
    def __init__(self, book_id , book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.is_issued = False

    def show_details(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Book Id :{self.book_id}")
        print(f"Book Name : {self.book_name}")
        print(f"Author Name : {self.author}")
        print(f"Status : {status}\n")

    @classmethod
    def add_books(cls):
        book_id = input("Enter your book Id :")
        book_name = input("Enter the book name :")
        author_name = input("Enter the author name :")
        book = cls(book_id, book_name, author_name)
        cls.books.append(book)
        print(f"{book_name} added successfully.")

    @classmethod
    def view_books(cls):
        if len(cls.books) == 0:
            print("No books added!")
            return
        print("--------Book Details---------\n")
        for book in cls.books:
            book.show_details()

    @classmethod
    def borrow_books(cls):
        book_id = input("Enter Book Id to borrow : ")
        
        for book in cls.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print("Book is already issued!")
                    return
                book.is_issued = True
                cls.issued_books.append(book)
                print(f"{book.book_name} borrowed successfully!")
                return
        print("Book not Found!")

    @classmethod
    def return_books(cls):
        book_id = input("Enter Book Id to return :")
        for book in cls.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    print("This Book was not issue!")
                book.is_issued = False
                cls.issued_books.remove(book)
                print(f"{book.book_name} returned successfully!")
                return
        print("Book not found!")

def menu():
    while True:
        print("<============= Library Management System ===========> ")
        print("1. Add Books.")
        print("2. View Available Books.")
        print("3. Borrow Books.")
        print("4. Return Books.")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            Library.add_books()
        elif choice == "2":
            Library.view_books()
        elif choice == "3":
            Library.borrow_books()
        elif choice == "4":
            Library.return_books()
        elif choice == "5":
            print("Exiting Library Management System......")
            break
        else:
            print("Invalid Choice!")
if __name__ == "__main__":
    menu()

