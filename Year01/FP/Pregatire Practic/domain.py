import datetime


class Tractor:
    def __init__(self, id_tractor, name, price, model, revision_date, is_deleted):
        self.__id = id_tractor
        self.__name = name
        self.__price = price
        self.__model = model
        self.__revision_date = revision_date
        self.__is_deleted = is_deleted

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getModel(self):
        return self.__model

    def getDate(self):
        return self.__revision_date

    def getIsDeleted(self):
        return self.__is_deleted

    def setIsDeleted(self):
        self.__is_deleted = True

    def isExpired(self):
        today_time = str(datetime.date.today()).split('-')
        tractor_date = self.__revision_date.split('/')
        if today_time[0] > tractor_date[2]:
            return True
        elif today_time[0] == tractor_date[2]:
            if today_time[1] > tractor_date[1]:
                return True
            elif today_time[1] == tractor_date[1]:
                if today_time[2] > tractor_date[0]:
                    return True
                return False

        return False

    def __str__(self):
        if self.isExpired():
            return (f"Id: {self.__id:<2} *Name: {self.__name:<25} Price: {self.__price:<25} "
                    f"Model: {self.__model:<25} Date: {self.__revision_date}")
        else:
            return (f"Id: {self.__id:<2} Name: {self.__name:<25} Price: {self.__price:<25} "
                    f"Model: {self.__model:<25} Date: {self.__revision_date}")
