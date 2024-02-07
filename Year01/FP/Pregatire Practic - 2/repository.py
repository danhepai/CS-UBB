from domain import Exam

class RepositoryMemory:
    def __init__(self):
        self.__exams = []

    def get_all_exams(self):
        return self.__exams

    def add_exam(self, exam):
        id_to_check = exam.getId()
        materie_to_check = exam.getMaterie()
        sesiune_to_check = exam.getSesiune()
        for obj in self.__exams:
            if obj.getId() == id_to_check:
                raise ValueError("Repo Error -> 16: ID already exists!")
            if obj.getMaterie() == materie_to_check and obj.getSesiune() == sesiune_to_check:
                raise ValueError("Repo Error -> 18: Session already exists!")

        self.__exams.append(exam)


class RepositoryFile(RepositoryMemory):
    def __init__(self, file_name):
        RepositoryMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__file_name, 'r') as file:
            for line in file:
                if line.strip() == '':
                    continue
                line = line.strip().split(';')
                examid = line[0]
                data = line[1]
                hour = line[2]
                materie = line[3]
                sesiune = line[4]
                exam = Exam(examid, data, hour, materie, sesiune, False)
                RepositoryMemory.add_exam(self, exam)


    def overwrite_data(self, exams):
        data_to_load = ""
        for exam in exams:
            string = f"{exam.getId()};{exam.getDate()};{exam.getHour()};{exam.getMaterie()};{exam.getSesiune()}"
            data_to_load += string + '\n'
        with open(self.__file_name, 'w') as file:
            file.write(data_to_load)

    def __save_to_file(self):
        exams = RepositoryMemory.get_all_exams(self)
        data_to_load = ""
        for exam in exams:
            string = f"{exam.getId()};{exam.getDate()};{exam.getHour()};{exam.getMaterie()};{exam.getSesiune()}"
            data_to_load += string + '\n'
        with open(self.__file_name, 'w') as file:
            file.write(data_to_load)

    def add_exam(self, exam):
        RepositoryMemory.add_exam(self, exam)
        self.__save_to_file()

