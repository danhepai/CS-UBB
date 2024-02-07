from domain import Tractor

class Service:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def srv_get_all_tractors(self):
        return self.__repo.repo_get_all_tractors()

    def srv_add_filter(self, text, number):
        tractor_filter = [text, number]
        self.__validator.validate_filter(text, number)
        return tractor_filter

    def srv_apply_filter(self, tractor_filter):
        tractors = self.srv_get_all_tractors()
        text = tractor_filter[0]
        max_price = int(tractor_filter[1])

        filter_result = ""
        if text == "" and max_price != -1:
            filter_result = ""
            for tractor in tractors:
                if max_price >= int(tractor.getPrice()) and not tractor.getIsDeleted():
                    filter_result += str(tractor)
        elif max_price == -1 and text != "":
            filter_result = ""
            for tractor in tractors:
                if (text in tractor.getName()) and not tractor.getIsDeleted():
                    filter_result += str(tractor)
        elif max_price != -1 and text != "":
            filter_result = ""
            for tractor in tractors:
                if (text in tractor.getName()) and (max_price >= int(tractor.getPrice())) and not tractor.getIsDeleted():
                    filter_result += str(tractor)
        else:
            for tractor in tractors:
                filter_result += str(tractor)

        return filter_result

    def srv_add(self, id_tractor, name, price, model, revision_date):
        tractor = Tractor(id_tractor, name, price, model, revision_date, False)
        self.__validator.validate_tractor(tractor)
        self.__repo.repo_add(tractor)


    def srv_delete(self, digit):
        tractors = self.srv_get_all_tractors()
        for tractor in tractors:
            if digit in tractor.getPrice() and not tractor.getIsDeleted():
                self.__repo.repo_deleteTractor(tractor.getId())

