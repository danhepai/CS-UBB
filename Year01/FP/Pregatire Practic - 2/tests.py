import unittest
from repository import RepositoryFile
from domain import Exam
from service import Service
from validators import Validator

class Teste(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryFile("test_file.txt")
        self.validator = Validator()
        self.service = Service(self.repo, self.validator)

    def test_domain(self):
        exam = Exam('1', '21.04', '18:30', 'asc', 'examen', False)
        self.assertEqual(exam.getId(), '1')
        self.assertEqual(exam.getDay(), '21')
        self.assertEqual(exam.getMonth(), '04')
        self.assertEqual(exam.getHour(), '18:30')
        self.assertEqual(exam.getMaterie(), 'asc')
        self.assertEqual(exam.getSesiune(), 'examen')

    def test_repository(self):
        exams = self.repo.get_all_exams()
        self.assertEqual(len(exams), 5)

        exam = exams[2]
        self.assertEqual(exam.getId(), '3')
        self.assertEqual(exam.getDay(), '07')
        self.assertEqual(exam.getMonth(), '02')
        self.assertEqual(exam.getHour(), '8:00')
        self.assertEqual(exam.getMaterie(), 'ANALIZA')
        self.assertEqual(exam.getSesiune(), 'restanta')

    def test_repository_add(self):
        no_of_exams_before_adding = len(self.repo.get_all_exams())
        exam = Exam('7', '21.04', '18:30', 'asc', 'examen', False)
        self.repo.add_exam(exam)
        exams = self.repo.get_all_exams()
        self.assertEqual(len(exams), no_of_exams_before_adding + 1)

        exam = exams[no_of_exams_before_adding]
        self.assertEqual(exam.getId(), '7')
        self.assertEqual(exam.getDay(), '21')
        self.assertEqual(exam.getMonth(), '04')
        self.assertEqual(exam.getHour(), '18:30')
        self.assertEqual(exam.getMaterie(), 'asc')
        self.assertEqual(exam.getSesiune(), 'examen')

    def test_service(self):
        month = 2
        day = 5
        test_string = "ID: 1 DATE: 06.02 HOUR: 09:00 MATERIE: FP SESIUNE: normal\n"
        self.assertEqual(self.service.get_all_next_day_exams(month, day), test_string)



