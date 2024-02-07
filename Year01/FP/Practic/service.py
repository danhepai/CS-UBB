from domain import Book

class Service:
    """
    Abstract data type -> class to incapsulate the service.
    """
    def __init__(self, repo):
        """
        Contructor for Service class
        :param repo: Repository -> Class
        """
        self.repo = repo
        self.__deleted_books = []
        self.__filtru = ["", -1]

    def getFilter(self):
        """
        Getter for the filter
        :return:
        """
        return self.__filtru

    def set_filter(self, text, num):
        """
        setter for the filter
        :param text: str
        :param num: str
        :return:
        """
        self.__filtru[0] = text
        if not num.isdigit() or num == "":
            self.__filtru[1] = -1
        else:
            self.__filtru[1] = num

        return self.__filtru

    def print_all_books(self):
        """
        Method to return all the books as a string
        :return: string - to be printed
        """
        books = self.repo.get_all_books()
        ans = ""
        for book in books:
            if not book.isDeleted():
                ans += str(book)
        return ans

    def print_books_with_filter(self, filtru):
        """
        Method to return all the books with filter as a string
        :return: string - to be printed
        """
        text = filtru[0]
        an = filtru[1]

        ans = ""
        books = self.repo.get_all_books()
        for book in books:
            if text in book.getTitle() and int(book.getYear()) < int(an) and not book.isDeleted():
                ans += str(book)

        return ans

    # def get_all_books(self):
    #     self.repo.get_all_books()

    def generate_id(self):
        """
        Method to generate an unique ID
        :return:
        """
        books = self.repo.get_all_books()
        ids = []
        for book in books:
            ids.append(int(book.getId()))

        return max(ids) + 1

    def add_book(self, idbook, title, autor, year):
        """
        Meethod to add a book by the user. Called by UI. Calls the repository
        :param idbook: str
        :param title: str
        :param autor: str
        :param year: str
        :return:
        """
        book = Book(idbook, title, autor, year, False)
        self.repo.add_book(book)

    def delete_book(self, cifra):
        """
        Meethod to delete a book by the user. Called by UI. Calls the repository
        :param cifra: str
        :return:
        """
        books = self.repo.get_all_books()
        self.__deleted_books.append([])
        for book in books:
            if cifra in book.getYear():
                book.setDeleted()
                self.__deleted_books[-1].append(book)

        self.repo.saveDeleted()

    def undo(self):
        """
        Method to undo the last deleted books
        :return:
        """
        if len(self.__deleted_books) != 0:
            for book in self.__deleted_books[-1]:
                book.setNotDeleted()

            self.__deleted_books.pop()

            self.repo.saveDeleted()

