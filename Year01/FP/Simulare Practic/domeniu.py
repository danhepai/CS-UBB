class Concurent:
    """
    Description: Abstract data type sa incapsulez informatii despre un concurent
    :param ID, nume, tara, data_nasterii
    """
    def __init__(self, id_concurent, nume, tara, data_nasterii):
        self.__id_concurent = id_concurent
        self.__nume = nume
        self.__tara = tara
        self.__data_nasterii = data_nasterii

    def getAn(self):
        """
        Description: Getter pentru anul concurentului
        :return: int
        """
        attributes = self.__data_nasterii.split('.')
        return int(attributes[2])

    def getId(self):
        """
        Description: Getter pentru ID concurentului
        :return: string
        """
        return self.__id_concurent

    def getTara(self):
        """
        Description: Getter pentru tara concurentului
        :return: string
        """
        return self.__tara

    def getNume(self):
        """
        Description: Getter pentru numele concurentului
        :return: string
        """
        return self.__nume

    def __str__(self):
        """
        Description: Suprascrierea functiei string
        :return:
        """
        return f"ID: {self.__id_concurent} NUME: {self.__nume.upper()} TARA: {self.__tara.upper()} DATA_NASTERII: {self.__data_nasterii}"


class Participare:
    """
    Description: Abstract data type sa incapsulez informatii despre o participare
    :param cod participare, id concurent, punctaj
    """
    def __init__(self, cod_participare, id_concurent, punctaj):
        self.__cod_participare = cod_participare
        self.__id_concurent = id_concurent
        self.__punctaj = punctaj

    def getIdConcurent(self):
        """
        Description: Getter pentru ID concurentului
        :return:
        """
        return self.__id_concurent

    def getPunctaj(self):
        """
        Description: Getter pentru punctajul participarii
        :return:
        """
        return self.__punctaj
