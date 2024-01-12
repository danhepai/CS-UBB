import random
import string

from domain.entities import Client


class ClientService:
    def __init__(self, repo_client, validator_client):
        self.__repo = repo_client
        self.__validator = validator_client

    def add_random_client(self, id_client, seed=None):
        """
        Description: Adds a random client to the repository
        :param id_client: string
        :param seed: Seed for the random generator
        :return:
        """
        random.seed(seed)
        name = ''.join(random.choices(string.ascii_lowercase, k=7))
        random.seed(seed)
        cnp = str(random.randint(1000000000000, 9999999999999))
        person = Client(id_client, name, cnp)
        self.__validator.validate(person)
        self.__repo.add_client(person)

    def create_client_and_add_it(self, id_client, name, CNP):
        """
        Description: Creates a client and adds it to the repository
        :param id_client: string
        :param name: string
        :param CNP: string
        :return:
        """
        person = Client(id_client, name, CNP)
        self.__validator.validate(person)
        self.__repo.add_client(person)

    def update_client_by_id(self, id_client, new_name, new_CNP):
        """
        Description: Updates a client by id
        :param id_client: string
        :param new_name: string
        :param new_CNP: string
        :return:
        """
        person = Client(id_client, new_name, new_CNP)
        self.__validator.validate(person)
        self.__repo.update_client(id_client, person)

    def print_all_clients(self):
        """
        Description: Prints all clients
        :return: string
        """
        clients = self.__repo.get_all_clients()
        string_of_clients = ""
        for person in clients:
            string_of_clients += str(person)
        return string_of_clients

    def search_client_by_name(self, name):
        """
        Description: Searches a client by name
        :param name: string
        :return: string of clients
        """
        clients = self.__repo.get_all_clients()
        string_of_clients = ""
        for person in clients:
            if person.getName() == name:
                string_of_clients += str(person)

        return string_of_clients

    def get_client_by_id(self, id_client):
        """
        Description: Gets a client by id
        :param id_client: string
        :return: client
        """
        return self.__repo.get_client(id_client)

    def get_all_clients_list(self):
        """
        Description: Gets all clients
        :return: string
        """
        return self.__repo.get_all_clients()
