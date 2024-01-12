from utils import sorting_algo
from domain.entities import RentDTO


class RentService:
    def __init__(self, repo_movie, repo_clients, repo_rent):
        self.__repo_movie = repo_movie
        self.__repo_clients = repo_clients
        self.__repo_rent = repo_rent

    def delete_movie_by_id(self, id_movie):
        """
        Description: Deletes a movie by id
        :param id_movie: string
        :return:
        """
        for rent in self.__repo_rent.get_all_rents_by_list_of_objects():
            if self.__repo_rent.get_rent_movie(rent).getId() == id_movie and self.__repo_rent.get_rent_status(rent):
                self.return_a_movie_by_a_client(self.__repo_rent.get_rent_movie(rent), self.__repo_rent.get_rent_client(rent))

        self.__repo_movie.delete_movie(id_movie)

    def delete_client_by_id(self, id_client):
        """
        Description: Deletes a client by id
        :param id_client: string
        :return:
        """
        for rent in self.__repo_rent.get_all_rents_by_list_of_objects():
            if self.__repo_rent.get_rent_client(rent).getId() == id_client and self.__repo_rent.get_rent_status(rent):
                self.return_a_movie_by_a_client(self.__repo_rent.get_rent_movie(rent), self.__repo_rent.get_rent_client(rent))

        self.__repo_clients.delete_client(id_client)

    def rent_a_movie_by_a_client(self, movie_to_rent, person_that_rents):
        """
        Description: Rents a movie by a client
        :param movie_to_rent: Movie
        :param person_that_rents: Client
        :return:
        """
        self.__repo_rent.add_client_film_to_rent_list(movie_to_rent, person_that_rents, True)

    def return_a_movie_by_a_client(self, movie_to_return, person_that_returns):
        """
        Description: Returns a movie by a client
        :param movie_to_return: Movie
        :param person_that_returns: Client
        :return:
        """
        self.__repo_rent.return_a_movie_by_a_client(movie_to_return, person_that_returns)

    def get_all_rents_as_string(self):
        """
        Description: Gets all rents as string
        :return: string
        """
        string = ""
        string += self.__repo_rent.get_all_rents_as_string()
        if string == "":
            return "There are no rents."
        else:
            return string

    def get_all_rents_by_list_of_objects(self):
        """
        Description: Gets all rents by list of objects
        :return: list
        """
        return self.__repo_rent.get_all_rents_by_list_of_objects()

    def get_rents_sorted_by_name(self):
        """
        Description: Gets rents sorted by name
        :return: string
        """
        rents = self.get_all_rents_by_list_of_objects()
        rents = sorting_algo.insertion_sort(rents, lambda x: self.__repo_rent.get_rent_client(x).getName())
        string = ""
        for rent in rents:
            if rent[2]:
                string += self.__repo_rent.get_a_rent_as_string(rent)

        return string

    def get_rents_sorted_by_number_of_movies_rented(self):
        """
        Description: Gets rents sorted by number of movies rented
        :return: string
        """
        clients = self.__repo_clients.get_all_clients()
        list_of_DTOs = []
        for client in clients:
            list_of_DTOs.append(RentDTO(client, len(self.__repo_rent.get_all_rents_by_a_client(client))))

        # list_of_DTOs.sort(key=lambda dto: dto.getNoOfRents(), reverse=True)
        list_of_DTOs = sorting_algo.comb_sort(list_of_DTOs, lambda x: x.getNoOfRents(), reverse=True)
        string = ""
        for DTO in list_of_DTOs:
            client_rents = self.__repo_rent.get_all_rents_by_a_client(DTO.getObject())
            for rent in client_rents:
                string += self.__repo_rent.get_a_rent_as_string(rent)

        return string

    def get_number_of_rents_by_every_client(self):
        """
        Description: Gets number of rents by every client
        :return: string
        """
        clients = self.__repo_clients.get_all_clients()
        list_of_DTOs = []
        for client in clients:
            list_of_DTOs.append(RentDTO(client, len(self.__repo_rent.get_all_rents_by_a_client(client))))

        # list_of_DTOs.sort(key=lambda dto: dto.getNoOfRents(), reverse=True)
        list_of_DTOs = sorting_algo.insertion_sort(list_of_DTOs, lambda x: x.getNoOfRents(), reverse=True)
        string = ""
        for DTO in list_of_DTOs:
            if DTO.getNoOfRents() > 0:
                string += DTO.stringClient()

        return string

    def get_most_rented_movies(self):
        """
        Description: Gets most rented movies
        :return: string
        """
        movies = self.__repo_movie.get_all_movies()
        list_of_DTOs = []
        for movie in movies:
            list_of_DTOs.append(RentDTO(movie, len(self.__repo_rent.get_all_rents_by_a_movie(movie))))

        # list_of_DTOs.sort(key=lambda dto: dto.getNoOfRents(), reverse=True)
        list_of_DTOs = sorting_algo.comb_sort(list_of_DTOs, lambda x: x.getObject()
                                              , lambda x, y: sorting_algo.compareMovies(x, y)
                                              , reverse=False)
        string = ""
        for DTO in list_of_DTOs:
            if DTO.getNoOfRents() > 0:
                string += DTO.stringMovie()

        return string

    def get_30_percent_clients_with_most_rents(self):
        """
        Description: Gets 30 percent clients with most rents
        :return: string
        """
        clients = self.__repo_clients.get_all_clients()
        list_of_DTOs = []
        for client in clients:
            list_of_DTOs.append(RentDTO(client, len(self.__repo_rent.get_all_rents_by_a_client(client))))

        # list_of_DTOs.sort(key=lambda dto: dto.getNoOfRents(), reverse=True)
        list_of_DTOs = sorting_algo.insertion_sort(list_of_DTOs, lambda x: x.getNoOfRents(), reverse=True)
        string = ""
        list_of_DTOs = list_of_DTOs[:int(len(list_of_DTOs) * 0.3)]
        for DTO in list_of_DTOs:
            if DTO.getNoOfRents() > 0:
                string += DTO.stringClient()

        return string
