import random
import string

from domain.entities import Movie


class MovieService:
    def __init__(self, repo_movie, validator_movie):
        self.__repo = repo_movie
        self.__validator = validator_movie

    def add_random_movie(self, id_movie, seed=None):
        """
        Description: Adds a random movie to the repository
        :param id_movie: string
        :param seed: Seed for the random generator
        :return:
        """
        random.seed(seed)
        title = ''.join(random.choices(string.ascii_lowercase, k=7))
        random.seed(seed)
        description = ''.join(random.choices(string.ascii_lowercase, k=10))
        random.seed(seed)
        movie_type = ''.join(random.choices(string.ascii_lowercase, k=6))
        film = Movie(id_movie, title, description, movie_type)
        self.__validator.validate(film)
        self.__repo.add_movie(film)

    def create_movie_and_add_it(self, id_movie, title, description, movie_type):
        """
        Description: Creates a movie and adds it to the repository
        :param id_movie: string
        :param title: string
        :param description: string
        :param movie_type: string
        :return:
        """
        film = Movie(id_movie, title, description, movie_type)
        self.__validator.validate(film)
        self.__repo.add_movie(film)

    def update_movie_by_id(self, id_to_update, new_title, new_desc, new_typ):
        """
        Description: Updates a movie by id
        :param id_to_update: string
        :param new_title: string
        :param new_desc: string
        :param new_typ: string
        :return:
        """
        film = Movie(id_to_update, new_title, new_desc, new_typ)
        self.__validator.validate(film)
        self.__repo.update_movie(id_to_update, film)

    def print_all_movies(self):
        """
        Description: Prints all movies
        :return: string
        """
        movies = self.__repo.get_all_movies()
        string_of_movies = ""
        for film in movies:
            string_of_movies += str(film)
        return string_of_movies

    def search_movie_by_title(self, title):
        """
        Description: Searches a movie by title
        :param title: string
        :return: string
        """
        movies = self.__repo.get_all_movies()
        string_of_movies = ""
        for film in movies:
            if film.getTitle() == title:
                string_of_movies += str(film)

        return string_of_movies

    def get_movie_by_id(self, id_movie):
        """
        Description: Gets a movie by id
        :param id_movie: string
        :return: Movie
        """
        return self.__repo.get_movie(id_movie)

    def get_all_movies_list(self):
        """
        Description: Gets all movies
        :return: list
        """
        return self.__repo.get_all_movies()

