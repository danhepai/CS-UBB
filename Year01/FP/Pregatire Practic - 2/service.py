from domain import Exam


class Service:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator
        self.__undo = self.__repo.get_all_exams()

    def get_all_next_day_exams(self, month, day):
        exams = self.__repo.get_all_exams()
        answer = ""
        for exam in exams:
            if int(exam.getMonth()) == int(month):
                if int(exam.getDay()) == int(day) + 1:
                    answer += str(exam)

        return answer

    def add_exam(self, data, hour, materie, sesiune):
        new_id = self.generate_id()
        exam = Exam(new_id, data, hour, materie, sesiune, False)
        self.__validator.validate(exam)
        exams = self.__repo.get_all_exams()
        for obj in exams:
            if obj.getSesiune() == exam.getSesiune() and obj.getMaterie() == exam.getMaterie():
                raise ValueError("Service -> 25: Same session for same materie!")
        self.__repo.add_exam(exam)

    def generate_id(self):
        exams = self.__repo.get_all_exams()
        ids = []
        for exam in exams:
            ids.append(int(exam.getId()))

        return max(ids) + 1

    def get_all_3_days_exams(self, day, month):
        exams = self.__repo.get_all_exams()
        answer = ""
        for exam in exams:
            if int(exam.getMonth()) == int(month):
                if int(exam.getDay()) == int(day) + 1 or int(exam.getDay()) == int(day) + 2 or int(
                        exam.getDay()) == int(day) + 3:
                    answer += str(exam)

        return answer

    def save_to_undo(self):
        exams = self.__repo.get_all_exams()
        self.__undo.append(exams)

    def undo(self):
        exams = self.__undo.pop()
        exams = self.__undo.pop()
        self.__repo.overwrite_data(exams)


    def export_in_file(self, file_name, chars):
        exams = self.__repo.get_all_exams()
        exams_to_export = []
        for exam in exams:
            if chars in exam.getMaterie():
                exams_to_export.append(exam)

        exams_to_export = sorted(exams_to_export, key=lambda obj: (int(obj.getMonth()), int(obj.getDay()),
                                                                   int(obj.getHour().split(':')[0]),
                                                                   int(obj.getHour().split(':')[1])),)
        answer = ""
        for exam in exams_to_export:
            answer += str(exam)

        with open('file_name', 'w') as file:
            file.write(answer)


