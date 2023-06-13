class Author:
    all = []
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract._author == self]
    
    def books(self):
        return [contract._book for contract in Contract.all if contract._author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract._royalties for contract in Contract.all if contract._author == self]) #good job visualizing this

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract._book == self]
    
    def authors(self):
        return [contract._author for contract in Contract.all if contract._book == self]


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.__setattr__("author", author)
        self.__setattr__("book", book)
        self.__setattr__("date", date)
        self.royalties = royalties  #did this the old fasion way
        self.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception

    # did it the non-decorator way to remember how it is done
    def get_royalties(self):
        return self._royalties
    
    def set_royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
        
    royalties = property(get_royalties, set_royalties)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key = lambda contract: contract._date)