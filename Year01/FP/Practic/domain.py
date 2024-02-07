class Book:
    """
    Abstract data type -> class to incapsulate attributes of an object Book.
    """
    def __init__(self, idbook, title, autor, year, is_deleted):
        """
        Contructor for a Book object
        :param idbook: str
        :param title: str
        :param autor: str
        :param year: str
        :param is_deleted: bool
        """
        self.__idbook = idbook
        self.__title = title
        self.__autor = autor
        self.__year = year
        self.__is_deleted = is_deleted

    def getId(self):
        """
        Getter for ID
        :return: str
        """
        return self.__idbook

    def getTitle(self):
        """
        Getter for title
        :return: str
        """
        return self.__title

    def getYear(self):
        """
        Getter for year
        :return: str
        """
        return self.__year

    def getAutor(self):
        """
        Getter for autor
        :return: str
        """
        return self.__autor

    def setDeleted(self):
        """
        Set the book to deleted
        :return:
        """
        self.__is_deleted = True

    def isDeleted(self):
        """
        Getter for deleted status
        :return: str
        """
        return self.__is_deleted

    def setNotDeleted(self):
        """
        Set the book to not deleted
        :return:
        """
        self.__is_deleted = False

    def __str__(self):
        """
        Overwrite the string function
        :return: str
        """
        return f"ID: {self.__idbook} TITLE: {self.__title} AUTOR: {self.__autor} AN: {self.__year}\n"
