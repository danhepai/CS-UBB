from domain.entities import Movie, Client


class RentRepositoryInMemory:
    def __init__(self):
        """
        I will store rents by a list [client, movie, isRented/notRented(True,False)]
        """
        self.__rent_list = []

    def add_client_film_to_rent_list(self, movie, client, is_rented):
        """
        Description: Adds a client and a movie to the rent list
        :param movie: Movie
        :param client: Client
        :param is_rented: Boolean
        :return:
        """
        self.__rent_list.append([client, movie, is_rented])

    def delete_pair_of_rented(self, movie, client):
        """
        Description: Deletes a pair of rented movie and client
        :param movie: Movie
        :param client: Client
        :return:
        """
        found = False
        for rent in self.__rent_list:
            if rent[0] == client and rent[1] == movie:
                rent[2] = False
                found = True

        if not found:
            raise Exception("Rent cannot be deleted because it does not exist.")

    def return_a_movie_by_a_client(self, movie_to_return, person_that_returns):
        """
        Description: Returns a movie by a client
        :param movie_to_return: Movie
        :param person_that_returns: Client
        :return:
        """
        found = False
        for rent in self.__rent_list:
            if rent[0] == person_that_returns and rent[1] == movie_to_return:
                if not rent[2]:
                    raise Exception("Rent cannot be returned because it was already.")
                else:
                    rent[2] = False
                    found = True

        if not found:
            raise Exception("Rent cannot be returned because it does not exist.")

    def get_all_rents_by_a_client(self, client):
        """
        Description: Gets all rents by a client
        :param client: Client
        :return:
        """
        list_of_rents_by_a_client = []
        for rent in self.__rent_list:
            if rent[0] == client and rent[2]:
                list_of_rents_by_a_client.append(rent)

        return list_of_rents_by_a_client

    def get_all_rents_by_a_movie(self, movie):
        """
        Description: Gets all rents by a movie
        :param movie: Movie
        :return:
        """
        list_of_rents_by_a_movie = []
        for rent in self.__rent_list:
            if rent[1] == movie and rent[2]:
                list_of_rents_by_a_movie.append(rent)

        return list_of_rents_by_a_movie

    def get_all_rents_as_string(self):
        """
        Description: Gets all rents as string
        :return: string
        """
        rents = ""
        for rent in self.__rent_list:
            if rent[2]:
                rents += (f"Client: {rent[0].getName()} (ID: {rent[0].getId()}) | Movie Rented: {rent[1].getTitle()}"
                          f" (ID: {rent[1].getId()})\n")

        return rents

    def get_a_rent_as_string(self, rent):
        """
        Description: Gets a rent as string
        :param rent: list
        :return: string
        """
        return f"Client: {rent[0].getName()} | Movie Rented: {rent[1].getTitle()}\n"

    def get_all_rents_by_list_of_objects(self):
        """
        Description: Gets all rents by list of objects
        :return: list
        """
        return self.__rent_list

    def get_rent_client(self, rent):
        """
        Description: Gets a rent client
        :param rent: list
        :return:
        """
        return rent[0]

    def get_rent_movie(self, rent):
        """
        Description: Gets a rent movie
        :param rent: list
        :return:
        """
        return rent[1]

    def get_rent_status(self, rent):
        """
        Description: Gets a rent status
        :param rent: list
        :return:
        """
        return rent[2]

    def get_number_of_movies_rented_by_client(self, client):
        """
        Description: Gets the number of movies rented by a client
        :param client: Client
        :return:
        """
        return len(self.get_all_rents_by_a_client(client))


class RentRepositoryFile(RentRepositoryInMemory):
    """
    Description: Class to handle file repository for rents
    Enherits from RentRepositoryInMemory
    """
    def __init__(self, file_name):
        RentRepositoryInMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Description: Loads the data from the file into the memory repository
        :return:
        """
        with open(self.__file_name, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                line = line.strip()
                attributes = line.split(";")
                movie = Movie(attributes[0], attributes[1], attributes[2], attributes[3])
                client = Client(attributes[4], attributes[5], attributes[6])
                is_rented = True if attributes[7] == "True" else False
                self.add_client_film_to_rent_list(movie, client, is_rented)

    def __save_to_file(self):
        """
        Description: Saves the data from the memory repository into the file
        :return:
        """
        with open(self.__file_name, "w") as file:
            for rent in self.get_all_rents_by_list_of_objects():
                file.write(f"{self.get_rent_movie(rent).getId()};{self.get_rent_movie(rent).getTitle()};"
                           f"{self.get_rent_movie(rent).getDescription()};{self.get_rent_movie(rent).getType()};"
                           f"{self.get_rent_client(rent).getId()};{self.get_rent_client(rent).getName()};"
                           f"{self.get_rent_client(rent).getCNP()};{self.get_rent_status(rent)}\n")

    def add_client_film_to_rent_list(self, movie, client, is_rented):
        """
        Description: Adds a client and a movie to the rent list
        :param movie: Movie
        :param client: Client
        :param is_rented: Boolean
        :return:
        """
        RentRepositoryInMemory.add_client_film_to_rent_list(self, movie, client, is_rented)
        self.__save_to_file()

    def delete_pair_of_rented(self, movie, client):
        """
        Description: Deletes a pair of rented movie and client
        :param movie: Movie
        :param client: Client
        :return:
        """
        RentRepositoryInMemory.delete_pair_of_rented(self, movie, client)
        self.__save_to_file()

    def return_a_movie_by_a_client(self, movie_to_return, person_that_returns):
        """
        Description: Returns a movie by a client
        :param movie_to_return: Movie
        :param person_that_returns: Client
        :return:
        """
        RentRepositoryInMemory.return_a_movie_by_a_client(self, movie_to_return, person_that_returns)
        self.__save_to_file()

    def get_all_rents_by_a_client(self, client):
        """
        Description: Gets all rents by a client
        :param client: Client
        :return: list
        """
        return RentRepositoryInMemory.get_all_rents_by_a_client(self, client)

    def get_all_rents_by_a_movie(self, movie):
        """
        Description: Gets all rents by a movie
        :param movie: Movie
        :return: list
        """
        return RentRepositoryInMemory.get_all_rents_by_a_movie(self, movie)

    def get_all_rents_as_string(self):
        """
        Description: Gets all rents as string
        :return: string
        """
        return RentRepositoryInMemory.get_all_rents_as_string(self)

    def get_a_rent_as_string(self, rent):
        """
        Description: Gets a rent as string
        :param rent: list
        :return: string
        """
        return RentRepositoryInMemory.get_a_rent_as_string(self, rent)

    def get_all_rents_by_list_of_objects(self):
        """
        Description: Gets all rents by list of objects
        :return: list
        """
        return RentRepositoryInMemory.get_all_rents_by_list_of_objects(self)

    def get_rent_client(self, rent):
        """
        Description: Gets a rent's client
        :param rent: list
        :return: Client
        """
        return RentRepositoryInMemory.get_rent_client(self, rent)

    def get_rent_movie(self, rent):
        """
        Description: Gets a rent's movie
        :param rent: list
        :return: Movie
        """
        return RentRepositoryInMemory.get_rent_movie(self, rent)

    def get_rent_status(self, rent):
        """
        Description: Gets a rent's status
        :param rent: list
        :return: boolean
        """
        return RentRepositoryInMemory.get_rent_status(self, rent)

    def get_number_of_movies_rented_by_client(self, client):
        """
        Description: Gets the number of movies rented by a client
        :param client: Client
        :return: int
        """
        return RentRepositoryInMemory.get_number_of_movies_rented_by_client(self, client)


