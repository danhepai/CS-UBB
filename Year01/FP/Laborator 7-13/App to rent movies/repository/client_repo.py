from domain.entities import Client


class ClientRepositoryInMemory:
    """
    Description: Class to handle memory repository for clients
    """

    def __init__(self):
        self.__clients = []

    def add_client(self, client):
        """
        Description: Adds a client to the repository
        :param client: Client
        :return:
        """
        id_client = client.getId()
        for person in self.__clients:
            if person.getId() == id_client:
                raise Exception("The ID already exists!\n")
        self.__clients.append(client)

    def add_client_recursive(self, client, clients):
        if len(clients) == 1 and clients[0].getId() != client.getId():
            self.__clients.append(client)
        if clients[0].getId() == client.getId():
            raise Exception("The ID already exists!\n")
        else:
            return self.add_client_recursive(client, clients[1:])

    def delete_client(self, id_client):
        """
        Description: Deletes a client to the repository
        :param id_client: String
        :return: -
        """
        id_found = False
        for client in self.__clients:
            if str(client.getId()) == id_client:
                self.__clients.remove(client)
                id_found = True

        if not id_found:
            raise Exception("The ID does not exist!\n")

    # nu setez cu setteri, ci trimit direct obiectul
    def update_client(self, id_client_to_update, person):
        """
        Description: Updates a client to the repository
        :param id_client_to_update: string
        :param person: Client
        :return: -
        """
        id_found = False
        for client in self.__clients:
            if client.getId() == id_client_to_update:
                client.setClient(person)
                id_found = True

        if not id_found:
            raise Exception("The ID does not exist!\n")

    def get_client(self, id_client):
        """
        Description: Gets a client from the repository by ID
        :param id_client: string
        :return: Client
        """
        for client in self.__clients:
            if client.getId() == id_client:
                return client

        raise Exception("The ID does not exist!\n")

    def get_all_clients(self):
        """
        Description: Gets all clients from repository
        :param: -
        :return: [Clients]
        """
        return self.__clients


class ClientRepositoryFile(ClientRepositoryInMemory):
    """
    Description: Class to handle file repository for clients
    Enherits from ClientRepositoryInMemory
    """

    def __init__(self, file_name):
        ClientRepositoryInMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Description: Opens the file and loads the data into the memory repository
        """
        with open(self.__file_name, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                line = line.strip()
                attributes = line.split(";")
                client = Client(attributes[0], attributes[1], attributes[2])
                ClientRepositoryInMemory.add_client(self, client)

    def __save_to_file(self):
        """
        Description: Opens the file and saves the data from the memory repository
        """
        with open(self.__file_name, "w") as file:
            for client in self.get_all_clients():
                line = client.getId() + ";" + client.getName() + ";" + client.getCNP() + "\n"
                file.write(line)

    def add_client(self, client):
        """
        Description: Adds a client to the repository
        """
        ClientRepositoryInMemory.add_client(self, client)
        self.__save_to_file()

    def delete_client(self, id_client):
        """
        Description: Deletes a client to the repository
        """
        ClientRepositoryInMemory.delete_client(self, id_client)
        self.__save_to_file()

    def update_client(self, id_client_to_update, person):
        """
        Description: Updates a client to the repository
        """
        ClientRepositoryInMemory.update_client(self, id_client_to_update, person)
        self.__save_to_file()

    def get_client(self, id_client):
        """
        Description: Gets a client from the repository by ID
        :param id_client: string
        :return: Client
        """
        return ClientRepositoryInMemory.get_client(self, id_client)

    def get_all_clients(self):
        """
        Description: Gets all clients from repository
        :param: -
        :return: [Clients]
        """
        return ClientRepositoryInMemory.get_all_clients(self)


class ClientRepositoryFileSecondary(ClientRepositoryInMemory):
    """
    Description: Class to handle file repository for clients
    Enherits from ClientRepositoryInMemory
    """

    def __init__(self, file_name):
        ClientRepositoryInMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Description: Opens the file and loads the data into the memory repository
        """
        with open(self.__file_name, "r") as file:
            lines = file.readlines()

            for i in range(0, len(lines), 3):
                client = Client(lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip())
                ClientRepositoryInMemory.add_client(self, client)

    def __save_to_file(self):
        """
        Description: Opens the file and saves the data from the memory repository
        """
        with open(self.__file_name, "w") as file:
            for client in self.get_all_clients():
                line = client.getId() + "\n" + client.getName() + "\n" + client.getCNP() + "\n"
                file.write(line)

    def add_client(self, client):
        """
        Description: Adds a client to the repository
        """
        ClientRepositoryInMemory.add_client(self, client)
        self.__save_to_file()

    def delete_client(self, id_client):
        """
        Description: Deletes a client to the repository
        """
        ClientRepositoryInMemory.delete_client(self, id_client)
        self.__save_to_file()

    def update_client(self, id_client_to_update, person):
        """
        Description: Updates a client to the repository
        """
        ClientRepositoryInMemory.update_client(self, id_client_to_update, person)
        self.__save_to_file()

    def get_client(self, id_client):
        """
        Description: Gets a client from the repository by ID
        :param id_client: string
        :return: Client
        """
        return ClientRepositoryInMemory.get_client(self, id_client)

    def get_all_clients(self):
        """
        Description: Gets all clients from repository
        :param: -
        :return: [Clients]
        """
        return ClientRepositoryInMemory.get_all_clients(self)
