from domeniu import Concurent, Participare


class RepoConcurenti:
    """
    Description: Abstract data type pentru repository-ul ce memoreaza concurenti
    :return:
    """
    def __init__(self, file_concurenti):
        self.__concurenti = []
        self.__file_name = file_concurenti
        self.__load_from_file()

    def __load_from_file(self):
        """
        Description: Loads data from the file
        :return:
        """
        with open(self.__file_name, 'r') as file:
            for line in file:
                line = line.strip().lower()
                attributes = line.split(',')
                id_concurent = attributes[0]
                nume = attributes[1]
                tara = attributes[2]
                data_nasterii = attributes[3]
                persoana = Concurent(id_concurent, nume, tara, data_nasterii)
                self.__concurenti.append(persoana)

    def get_toti_concurentii(self):
        """
        Description: Getter pentru totii concurentii
        :return: list
        """
        return self.__concurenti

    def get_concurent_by_id(self, my_id):
        """
        Description: Getter pentru numele concurentului
        :return: object Concurent
        """
        for concurent in self.__concurenti:
            if concurent.getId() == my_id:
                return concurent


class RepoParticipare:
    """
    Description: Abstract data type pentru repository-ul ce memoreaza participari
    :return:
    """
    def __init__(self, file_participare):
        self.__participari = []
        self.__file_name = file_participare
        self.__load_from_file()

    def __load_from_file(self):
        """
        Description: Loads data from the file
        :return:
        """
        with open(self.__file_name, 'r') as file:
            for line in file:
                line = line.strip().lower()
                attributes = line.split(',')
                cod_participare = attributes[0]
                id_concurent = attributes[1]
                punctaj = attributes[2]
                my_participare = Participare(cod_participare, id_concurent, punctaj)
                self.__participari.append(my_participare)

    def get_toate_participarile(self):
        """
        Description: Getter pentru toate participarile
        :return: list
        """
        return self.__participari
