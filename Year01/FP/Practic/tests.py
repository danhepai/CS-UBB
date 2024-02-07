import unittest
from repo import RepoInFile
from service import Service
from domain import Book


class Teste(unittest.TestCase):
    """
    Abstract data type -> class to incapsulate the tests. Using unittest
    """
    def setUp(self):
        """
        SetUp class to prepare test. Setting repository and service
        :return:
        """
        self.repo = RepoInFile("test_data.txt")
        self.service = Service(self.repo)

    def test_domain(self):
        """
        Method to test the methods of object book
        :return:
        """
        book = Book('1', 'bom', 'yo', '1999', False)
        self.assertEqual(book.getId(), '1')
        self.assertEqual(book.getTitle(), 'bom')
        self.assertEqual(book.getAutor(), 'yo')
        self.assertEqual(book.getYear(), '1999')
        self.assertEqual(book.isDeleted(), False)

        book.setDeleted()
        self.assertEqual(book.isDeleted(), True)

    def test_repo_get_add_book(self):
        """
        Method to test the add method & delete method of repository
        :return:
        """
        books = self.repo.get_all_books()
        n = len(books)
        idb = self.service.generate_id()
        book = Book(f'{idb}', 'bom', 'yo', '1999', False)
        self.repo.add_book(book)
        books = self.repo.get_all_books()
        self.assertEqual(len(books), n + 1)
        self.service.delete_book('1999')
        books = self.repo.get_all_books()
        undeleted_books = 0
        for book in books:
            if not book.isDeleted():
                undeleted_books += 1
        self.assertEqual(undeleted_books, n)

    def test_service_print_books(self):
        """
        Method to test the print books method of service
        :return:
        """
        books_str = self.service.print_all_books()
        string_to_test = ('ID: 1 TITLE: TEN AUTOR: CHRIS AN: 2021\n'
                          'ID: 2 TITLE: YO AUTOR: DAN AN: 2012\n'
                          'ID: 3 TITLE: HSDA AUTOR: NFA AN: 1978\n'
                          'ID: 4 TITLE: DBUCXIA AUTOR: FADC AN: 1988\n'
                          'ID: 5 TITLE: DBUCXIA AUTOR: 2 AN: 1988\n')

        self.assertEqual(books_str, string_to_test)

    def test_print_books_with_filter(self):
        """
        Method to test the print books method of service with filter on
        :return:
        """
        filtru = ['CX', '2020']
        string_to_test = self.service.print_books_with_filter(filtru)
        test_string = "ID: 4 TITLE: DBUCXIA AUTOR: FADC AN: 1988\nID: 5 TITLE: DBUCXIA AUTOR: 2 AN: 1988\n"
        self.assertEqual(string_to_test, test_string)

        filtru = ['', '1']
        string_to_test = self.service.print_books_with_filter(filtru)
        test_string = ""
        self.assertEqual(string_to_test, test_string)

    def test_service_add_book(self):
        """
        Method to test the add book method of service
        :return:
        """
        books = self.repo.get_all_books()
        n = len(books)
        self.service.add_book('10', 'aa', 'eu', '3883')
        self.assertEqual(len(self.repo.get_all_books()), n + 1)
        self.service.delete_book('3883')
        books = self.repo.get_all_books()
        undeleted_books = 0
        for book in books:
            if not book.isDeleted():
                undeleted_books += 1
        self.assertEqual(undeleted_books, n)

    def test_undo(self):
        """
        Method to test the undo method functionality
        :return:
        """
        books = self.repo.get_all_books()
        n = len(books)
        undeleted_books = 0
        for book in books:
            if not book.isDeleted():
                undeleted_books += 1
        self.assertEqual(undeleted_books, n)

        self.service.delete_book('3333')
        undeleted_books = 0
        for book in books:
            if not book.isDeleted():
                undeleted_books += 1
        self.assertEqual(undeleted_books, n)

        self.service.undo()
        undeleted_books = 0
        for book in books:
            if not book.isDeleted():
                undeleted_books += 1
        self.assertEqual(undeleted_books, n)


if __name__ == "__main__":
    unittest.main()
