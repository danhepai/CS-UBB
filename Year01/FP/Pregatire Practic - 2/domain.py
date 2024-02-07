class Exam:
    def __init__(self, examid, data, hour, materie, sesiune, is_deleted):
        self.__id = examid
        self.__data = data
        self.__hour = hour
        self.__materie = materie
        self.__sesiune = sesiune
        self.__is_deleted = is_deleted

    def getId(self):
        return self.__id

    def getMaterie(self):
        return self.__materie

    def getSesiune(self):
        return self.__sesiune

    def getDay(self):
        return self.__data.split('.')[0]

    def getMonth(self):
        return self.__data.split('.')[1]

    def getDate(self):
        return self.__data

    def getHour(self):
        return self.__hour


    def __str__(self):
        return f"ID: {self.__id} DATE: {self.__data} HOUR: {self.__hour} MATERIE: {self.__materie} SESIUNE: {self.__sesiune}\n"

