from datetime import date

def menu():
    print("App to manage exams:")
    print("add: add examen")
    print("set: set a date")
    print("export: export")
    print("quit/exit")

class Ui:
    def __init__(self, service):
        self.__service = service
        self.__commands = {
            "add": self.__ui_add_exam,
            "set": self.__ui_set_date,
            "export": self.__ui_export_in_file,
            "undo": self.__ui_undo
        }
        self.__3_days_exams = ""


    def __ui_next_day_exams(self):
        today_date = date.today()
        day = today_date.day
        month = today_date.month
        print(self.__service.get_all_next_day_exams(month, day))

    def __ui_add_exam(self):
        end = True
        while end:
            try:
                data = input("Date: ")
                hour = input("Hour: ")
                materie = input("Materie: ")
                sesiune = input("Sesiune: ")
                self.__service.add_exam(data, hour, materie, sesiune)
                print("Hooray. Added")
                self.__ui_save_to_undo()
                end = False
            except ValueError as ve:
                print(ve)

    def __ui_set_date(self):
        end = True
        while end:
            try:
                data = input("Date: ")
                data = data.strip().split('.')
                if len(data) != 2:
                    print("UI -> 48: Invalid date. Try again")
                else:
                    if not 1 <= int(data[0]) <= 31 or not 1 <= int(data[1]) <= 12:
                        print("UI -> 51: Invalid date. Try again")
                    else:
                        answers = self.__service.get_all_3_days_exams(data[0], data[1])
                        print(answers)
                        self.__3_days_exams = "Upcoming examns in 3 days:\n" + answers
                        end = False
            except ValueError as ve:
                print(ve)


    def __ui_export_in_file(self):
        end = True
        while end:
            try:
                file_name = input("File name: ")
                file_name += ".txt"
                chars = input("Characters: ")
                self.__service.export_in_file(file_name, chars)
                print("Done!")
                end = False
            except ValueError as ve:
                print(ve)

    def __ui_save_to_undo(self):
        self.__service.save_to_undo()

    def __ui_undo(self):
        self.__service.undo()
        print("Undo done!")


    def run(self):
        menu()
        self.__ui_next_day_exams()
        while True:
            cmd = input(">>> ").strip().lower()
            if self.__3_days_exams != "":
                print(self.__3_days_exams)
            if cmd == 'quit' or cmd == 'exit':
                return
            if cmd not in self.__commands:
                print("No command.")
            else:
                try:
                    self.__commands[cmd]()
                except ValueError as ve:
                    print(ve)

