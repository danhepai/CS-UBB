def menu():
    """
    Description: Prints the menu on the console
    :return:
    """
    print("MENU")
    print("1. Afisarea concurentilor nascuti dupa un an anume (Command: 1)")
    print("2. Afisarea clasamentului pe tari (Command 2)")
    print("Exit / Quit")


class ConsoleUI:
    """
    Description: Abstract data to interact with the user
    """
    def __init__(self, service):
        self.__srv = service
        self.__commands = {
            '1': self.__ui_afisare_concurenti_dupa_an,
            '2': self.__ui_afisare_clasament_pe_tari
        }

    def __ui_afisare_concurenti_dupa_an(self):
        """
        Description: Afiseaza toti concurentii care s-au nascut dupa un an introdus de utilizator
        :return:
        """
        end = True
        while end:
            print("Introduceti un an: ")
            an = input(">>> ")
            if not an.isdigit() or len(an) != 4:
                print("Invalid year.")
            else:
                try:
                    print(self.__srv.afisare_concurenti_dupa_an(an))
                    end = False
                except Exception as ex:
                    print(ex)

    def __ui_afisare_clasament_pe_tari(self):
        """
        Description: Afiseaza clasamentul tarilor cu punctajele lor
        :return:
        """
        end = True
        while end:
            try:
                print(self.__srv.afisare_clasament_pe_tari())
                end = False
            except Exception as ex:
                print(ex)

    def run(self):
        """
        Description: Metoda ce porneste programul
        :return:
        """
        menu()
        while True:
            cmd = input(">>> ").strip().lower()
            if cmd == 'exit' or cmd == 'quit':
                return
            elif cmd in self.__commands:
                self.__commands[cmd]()
            else:
                print("Invalid option.")
