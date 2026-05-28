

class library:
    def __init__(self):
        self.noBooks = 0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def showinfo(self):
        print(f"the library has {self.noBooks} books . the books are")
        for book in self.books:
            print(book)


l1=library()
l1.addBook("harry potter")
l1.addBook("math")
l1.addBook("harry potter1")
l1.addBook("harry potter4")

l1.showinfo()                



































