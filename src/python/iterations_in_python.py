class Library:
    book_shelf = {}
    index = 0
    def __int__(self):
        pass
    def add_book(self,book):
        self.book_shelf[book.name] = book.author
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        length = len(self.book_shelf)
        items = self.book_shelf.items()
        if self.index >= length:
            raise StopIteration
        
        self.index += 1
        return "hi"


class Books:
    def __init__(self,name,author):
        self.name = name
        self.author = author
    def __iter__(self):
        pass

if __name__ == "__main__":
    pie = Books("pie","richard wilson")
    hero = Books("hero","namn")
    dim = Books("dim","komal")
    lib = Library()
    lib.add_book(pie)
    lib.add_book(hero)
    lib.add_book(dim)
    for x in lib:
        print(x)
    try:
        m = iter(lib)
        print(id(m)==id(lib))
        while(True):
            print(next(m))

    except(StopIteration):
        print("Stop Iteration occured")

        
        