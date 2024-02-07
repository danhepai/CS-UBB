def menu():
    print("Aplicatie de gestiune a cartilor intr-o biblioteca")
    print("Optiuni:")
    print("1. add: id, titlu, autor, anAparitie")
    print("2. delete: cifra")
    print("3. filter: titlu, anAparitie")
    print("4. undo")
    print("quit/exit")


class UI:
    """
    Abstract data type -> class to incapsulate the UI
    """
    def __init__(self, srv):
        """
        Contructor for UI class
        :param srv: Service -> Object
        """
        self.__srv = srv
        self.__commands = {
            "add": self.__ui_add_book,
            "delete": self.__ui_delete_book,
            "filter": self.__ui_set_filtru,
            "undo": self.__ui_undo
        }
        self.__filtru = ["", -1]


    def __ui_undo(self):
        """
        Method to undo the last deleted books. Calls Service
        :return:
        """
        self.__srv.undo()

    def generate_id(self):
        """
        Method to generate a unique ID
        :return: str
        """
        return self.__srv.generate_id()

    def __ui_print_all_books(self):
        """
        Print all the books on the screen
        :return:
        """
        print(self.__srv.print_all_books())

    def __ui_print_books_with_filter(self):
        """
        Print all the books with filter on the screen
        :return:
        """
        filtru = self.__srv.getFilter()
        print(self.__srv.print_books_with_filter(filtru))

    def __ui_add_book(self):
        """
        Gets data from the user to add a book
        :return: raises Value Error if the user data is incorrect
        """
        end = True
        while end:
            try:
                idbook = input("Id: ").strip().lower()
                while idbook == "":
                    idbook = input("Id: ").strip().lower()
                title = input("Title: ").strip().lower()
                while title == "":
                    title = input("Title: ").strip().lower()
                autor = input("Autor: ").strip().lower()
                while autor == "":
                    autor = input("Autor: ").strip().lower()
                year = input("An aparitie: ").strip().lower()
                while year == "" or not year.isdigit():
                    year = input("An aparitie: ").strip().lower()
                self.__srv.add_book(idbook, title, autor, year)
                print("Hooray. Added")
                end = False
            except ValueError as ve:
                print(ve)

    def __ui_delete_book(self):
        """
        Gets data from the user to delete a book/books
        :return: raises Value Error if the user data is incorrect
        """
        end = True
        while end:
            try:
                cifra = input("Cifra: ").strip().lower()
                self.__srv.delete_book(cifra)
                print("Hooray. Deleted")
                end = False
            except ValueError as ve:
                print(ve)

    def __ui_set_filtru(self):
        """
        Gets data from the user to set a filter
        :return: raises Value Error if the user data is incorrect
        """
        end = True
        while end:
            try:
                print("Filtru")
                text = input("Text: ").strip().lower()
                num = input("Num: ").strip().lower()
                filtru = self.__srv.set_filter(text, num)
                print("Hooray. Filter set")
                print(f"FILTRU TEXT: {filtru[0]} NUM: {filtru[1]}")
                self.__ui_print_books_with_filter()
                end = False
            except ValueError as ve:
                print(ve)

    def run(self):
        """
        Method to start the program. Is callable in main.
        :return:
        """
        menu()
        while True:
            if self.__srv.getFilter() == ["", -1]:
                self.__ui_print_all_books()
            cmd = input(">>> ").strip().lower()
            if cmd == "quit" or cmd == "exit":
                print("Ceao")
                return
            if cmd not in self.__commands:
                print("UI: Invalid option")
            else:
                if self.__srv.getFilter() != ["", -1]:
                    self.__ui_print_books_with_filter()
                self.__commands[cmd]()


