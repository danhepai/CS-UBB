import unittest
from service import Service
from repository import RepoConcurenti, RepoParticipare
from domeniu import Concurent, Participare


class Teste(unittest.TestCase):
    def setUp(self):
        """
        Description: Set Up pentru teste
        :return:
        """
        self.repo_concurenti = RepoConcurenti("test_file_concurenti.txt")
        self.repo_participari = RepoParticipare("test_file_participari.txt")
        self.srv = Service(self.repo_concurenti, self.repo_participari)

    def test_domeniu_concurent(self):
        """
        Description: Testeaza metodele din domeniul concurentului
        :return:
        """
        concurent_test = Concurent('3', 'Maria', 'Romania', '13.06.2000')
        self.assertEqual(concurent_test.getId(), '3')
        self.assertEqual(concurent_test.getAn(), 2000)
        self.assertEqual(concurent_test.getTara(), 'Romania')
        self.assertEqual(concurent_test.getNume(), 'Maria')

        string = "ID: 3 NUME: MARIA TARA: ROMANIA DATA_NASTERII: 13.06.2000"
        self.assertEqual(str(concurent_test), string)

    def test_domeniu_participare(self):
        """
        Description: Testeaza metodele din domeniul participarii
        :return:
        """
        participare_test = Participare('3','4','69')
        self.assertEqual(participare_test.getPunctaj(), '69')
        self.assertEqual(participare_test.getIdConcurent(), '4')

    def test_repo_concurenti(self):
        """
        Description: Testeaza metodele din repository-ul concurentului
        :return:
        """
        concurenti = self.repo_concurenti.get_toti_concurentii()
        self.assertEqual(len(concurenti), 3)

        string = ("ID: 1 NUME: POPESCU TARA: ROMANIA DATA_NASTERII: 13.09.2000"
                  "ID: 2 NUME: DAN TARA: ANGLIA DATA_NASTERII: 21.04.2004"
                  "ID: 3 NUME: MARIA TARA: ROMANIA DATA_NASTERII: 13.06.2000")

        test_string = ""
        for concurent in concurenti:
            test_string += str(concurent)

        self.assertEqual(test_string, string)

        concurent_dupa_id = self.repo_concurenti.get_concurent_by_id('1')
        self.assertEqual(concurent_dupa_id.getAn(), 2000)
        self.assertEqual(concurent_dupa_id.getId(), '1')
        self.assertEqual(concurent_dupa_id.getTara(), 'romania')
        self.assertEqual(concurent_dupa_id.getNume(), 'popescu')

    def test_repo_participare(self):
        """
        Description: Testeaza metodele din repository-ul participarilor
        :return:
        """
        participari = self.repo_participari.get_toate_participarile()
        self.assertEqual(len(participari), 3)

    def test_service(self):
        """
        Description: Testeaza metodele din service
        :return:
        """
        test_string = self.srv.afisare_concurenti_dupa_an('1900')
        second_test_string = ("ID: 1 NUME: POPESCU TARA: ROMANIA DATA_NASTERII: 13.09.2000\n"
                              "ID: 2 NUME: DAN TARA: ANGLIA DATA_NASTERII: 21.04.2004\n"
                              "ID: 3 NUME: MARIA TARA: ROMANIA DATA_NASTERII: 13.06.2000\n")

        self.assertEqual(test_string, second_test_string)

        test_string = self.srv.afisare_clasament_pe_tari()
        second_test_string = "Tara: ANGLIA Puntaj: 900\nTara: ROMANIA Puntaj: 250\n"

        self.assertEqual(test_string, second_test_string)


if __name__ == "__main__":
    unittest.main()