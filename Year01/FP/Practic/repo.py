from domain import Book

class RepoInMemory:
    """
    Abstract data type -> class to incapsulate the repository which uses the memory.
    """
    def __init__(self):
        """
        Contructor for Repository class
        """
        self.__books = []

    def get_all_books(self):
        """
        Getter for all the books
        :return: list of objects
        """
        return self.__books

    def add_book(self, book):
        """
        Method to add a book object in the memory
        :param book: Book
        :return: raises Value Error if it finds a duplicated ID
        """
        books = self.get_all_books()
        for obj in books:
            if obj.getId() == book.getId():
                raise ValueError("REPO: Same ID!")

        self.__books.append(book)

class RepoInFile(RepoInMemory):
    """
    Abstract data type -> class to incapsulate the repository which uses the file.
    """
    def __init__(self, file_name):
        """
        Contructor for the repository which handles the file
        :param file_name: str
        """
        RepoInMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads the books from the file
        :return:
        """
        with open(self.__file_name, 'r') as file:
            for line in file:
                if line.strip() == "":
                    continue
                line = line.strip().split(';')
                book = Book(line[0], line[1], line[2], line[3], False)
                RepoInMemory.add_book(self, book)

    def __save_to_file(self):
        """
        Save the books from memory in the file
        :return:
        """
        data = ""
        books = self.get_all_books()
        for book in books:
            if not book.isDeleted():
                data += f"{book.getId()};{book.getTitle()};{book.getAutor()};{book.getYear()}\n"

        with open(self.__file_name, 'w') as file:
            file.write(data)

    def saveDeleted(self):
        """
        Save the books from memory in the file after the user deleted one/multiple books
        :return:
        """
        self.__save_to_file()

    def get_all_books(self):
        """
        Method to get all the books from the memory
        :return:
        """
        return RepoInMemory.get_all_books(self)

    def add_book(self, book):
        """
        Method to add a book to the file
        :param book:
        :return:
        """
        RepoInMemory.add_book(self, book)
        self.__save_to_file()
