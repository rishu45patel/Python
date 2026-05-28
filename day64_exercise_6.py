
# write a library class with no_of_books and books as two instance variables.
  # write a program to create a library from this library class and show how you can print all books,add a book and
# get the number of books using diffrerent methods.show that your program doesnt persist the books after the program is stopped

#  i am try this question but i am not successfully code write .so i can take halp of ai



class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    # add book method
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f'"{book_name}" added successfully.')

    # show all books
    def show_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print(book)

    # show total number of books
    def get_number_of_books(self):
        print(f"\nTotal books: {self.no_of_books}")


# creating object
library = Library()

# adding books
library.add_book("Python")
library.add_book("Java")
library.add_book("C++")

# printing all books
library.show_books()

# printing total books
library.get_number_of_books()






















































