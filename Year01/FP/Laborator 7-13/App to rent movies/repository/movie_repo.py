from domain.entities import Movie


class MovieRepositoryInMemory:
    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        """
        Description: Adds a movie to the repository
        :param movie: Movie
        :return: -
        """
        id_movie = movie.getId()
        for film in self.__movies:
            if film.getId() == id_movie:
                raise Exception("The ID already exists!\n")
        self.__movies.append(movie)

    def delete_movie(self, id_movie):
        """
        Description: Deletes a movie to the repository by ID
        :param id_movie: string
        :return: -
        """
        id_found = False
        for film in self.__movies:
            if str(film.getId()) == id_movie:
                self.__movies.remove(film)
                id_found = True

        if not id_found:
            raise Exception("The ID does not exist!\n")

    def update_movie(self, id_movie_to_update, film):
        """
        Description: Updates a movie to the repository
        :param film: Movie
        :param id_movie_to_update: string
        :return: -
        """
        id_found = False
        for movie in self.__movies:
            if movie.getId() == id_movie_to_update:
                movie.setMovie(film)
                id_found = True

        if not id_found:
            raise Exception("The ID does not exist!\n")

    def get_movie(self, id_film):
        """
        Description: Gets a movie from the repository by ID
        :param id_film: string
        :return: Movie
        """
        for film in self.__movies:
            if film.getId() == id_film:
                return film

        raise Exception("The ID does not exist!\n")

    def get_movie_recursive(self, id_film, movies):
        if len(movies) == 1 and movies[0].getId() != id_film:
            raise Exception("The ID does not exist!\n")
        if movies[0].getId() == id_film:
            return movies[0]
        else:
            return self.get_movie_recursive(id_film, movies[1:])

    def get_all_movies(self):
        """
        Description: Gets all movies from the repository by ID
        """
        return self.__movies


class MovieRepositoryFile(MovieRepositoryInMemory):
    """
    Description: Class to handle file repository for movies
    Enherits from MovieRepositoryInMemory
    """
    def __init__(self, file_name):
        MovieRepositoryInMemory.__init__(self)
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        """
        Description: Loads movies from file
        :return:
        """
        with open(self.__file_name, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                line = line.strip()
                attributes = line.split(";")
                movie = Movie(attributes[0], attributes[1], attributes[2], attributes[3])
                MovieRepositoryInMemory.add_movie(self, movie)

    def __save_to_file(self):
        """
        Description: Saves movies to file
        :return:
        """
        with open(self.__file_name, "w") as file:
            for movie in self.get_all_movies():
                line = movie.getId() + ";" + movie.getTitle() + ";" + movie.getDescription() + ";" + movie.getType() + "\n"
                file.write(line)

    def add_movie(self, movie):
        """
        Description: Adds a movie to the repository
        :param movie: Movie
        :return:
        """
        MovieRepositoryInMemory.add_movie(self, movie)
        self.__save_to_file()

    def delete_movie(self, id_movie):
        """
        Description: Deletes a movie to the repository by ID
        :param id_movie: string
        :return:
        """
        MovieRepositoryInMemory.delete_movie(self, id_movie)
        self.__save_to_file()

    def update_movie(self, id_movie_to_update, film):
        """
        Description: Updates a movie to the repository
        :param id_movie_to_update: string
        :param film: Movie
        :return:
        """
        MovieRepositoryInMemory.update_movie(self, id_movie_to_update, film)
        self.__save_to_file()

    def get_movie(self, id_movie):
        """
        Description: Gets a movie from the repository by ID
        :param id_movie: string
        :return:
        """
        return MovieRepositoryInMemory.get_movie(self, id_movie)

    def get_all_movies(self):
        """
        Description: Gets all movies from the repository
        :return:
        """
        return MovieRepositoryInMemory.get_all_movies(self)
