from domain import Tractor

class RepoInMemory:
    def __init__(self):
        self.__tractors = []

    def repo_add(self, tractor):
        id_tractor = tractor.getId()
        for objs in self.__tractors:
            if objs.getId() == id_tractor:
                raise Exception("The ID already exists!")
        self.__tractors.append(tractor)

    def repo_deleteTractor(self, id_tractor):
        id_found = False
        for tractor in self.__tractors:
            if tractor.getId() == id_tractor:
                id_found = True
                self.__tractors.remove(tractor)

        if not id_found:
            raise Exception("The ID does not exist!\n")

    def repo_get_all_tractors(self):
        return self.__tractors


class RepoInFile(RepoInMemory):
    def __init__(self, file_name):
        RepoInMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__file_name, 'r') as file:
            for line in file:
                if line.strip() == "":
                    continue
                line.strip()
                attributes = line.split(';')
                tractor = Tractor(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], False)
                self.repo_add(tractor)

    def __save_to_file(self):
        with open(self.__file_name, 'w') as file:
            for tractor in self.repo_get_all_tractors():
                line = f"{tractor.getId()};{tractor.getName()};{tractor.getPrice()};{tractor.getModel()};{tractor.getDate()}"
                file.write(line)

    def repo_add(self, tractor):
        RepoInMemory.repo_add(self, tractor)
        self.__save_to_file()

    def repo_deleteTractor(self, id_tractor):
        RepoInMemory.repo_deleteTractor(self, id_tractor)
        self.__save_to_file()