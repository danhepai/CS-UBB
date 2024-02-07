from utils import generate_id


def menu():
    print("Welcome to your TRACTOARE app :)")
    print("Options available:")
    print("1. add : id, name, price, model, revision-expire-date")
    print("2. delete: digit")
    print("3. filter: text, number")
    print("4. undo")
    print("5. exit/quit")


class ConsoleUi:
    def __init__(self, service):
        self.__srv = service
        self.__commands = {
            "add": self.__ui_add,
            "delete": self.__ui_delete,
            "filter": self.__ui_add_filter,
            "undo": 0
        }
        self.__filter = ["", 100000000000]

    def __ui_add(self):
        self.__ui_apply_filter()
        end = True
        while end:
            name = input("Introduce the name: ")
            price = input("Introduce the price: ")
            model = input("Introduce the model: ")
            revision_date = input("Introduce the date when the revision expires: ")
            try:
                id_tractor = generate_id(self.__srv.srv_get_all_tractors())
                self.__srv.srv_add(id_tractor, name, price, model, revision_date)
                print("Tractor added!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_delete(self):
        self.__ui_apply_filter()
        end = True
        while end:
            digit = input("Introduce a digit. All the tractors' prices containing that digit will be deleted: ")
            try:
                print(self.__srv.srv_delete(digit))
                end = False
            except Exception as ex:
                print(ex)

    def __ui_add_filter(self):
        end = True
        while end:
            text = input("Introduce a text filter: ")
            number = input("Introduce a number to filter prices below that: ")
            try:
                self.__filter = self.__srv.srv_add_filter(text, number)
                end = False
                self.__ui_apply_filter()
            except Exception as ex:
                print(ex)

    def __ui_apply_filter(self, ):
        print(f"Filter -> text: {self.__filter[0]} max_price: {self.__filter[1]}")
        tractor_filter = self.__filter
        print(self.__srv.srv_apply_filter(tractor_filter))

    def run(self):
        menu()
        while True:
            cmd = input(">>> ").strip().lower()
            if cmd == "exit" or cmd == "quit":
                return

            if cmd in self.__commands:
                try:
                    self.__commands[cmd]()
                except Exception as ex:
                    print(ex)
            else:
                print("Invalid menu. Try again:")

