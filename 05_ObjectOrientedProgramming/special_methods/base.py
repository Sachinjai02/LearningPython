# DUNDER METHODS

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Book {self.title} by {self.author} has {self.pages} pages'

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


my_book = Book('Python rocks', 'ABC', 400)
print(my_book)
print(len(my_book))
del my_book
