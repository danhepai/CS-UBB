class Movie:
    """
    Description: Abstract data type for movies.
    Domain: {id, title, description, type}
    """
    def __init__(self, movie_id, title, description, movie_type):
        self.__movie_id = movie_id
        self.__title = title
        self.__description = description
        self.__movie_type = movie_type

    def getId(self):
        """
        Description: Getter for the movie's id
        :return: string
        """
        return str(self.__movie_id)

    def getTitle(self):
        """
        Description: Getter for the movie's title
        :return: string
        """
        return self.__title

    def getDescription(self):
        """
        Description: Getter for the movie's description
        :return: string
        """
        return self.__description

    def getType(self):
        """
        Description: Getter for the movie's type
        :return: string
        """
        return self.__movie_type

    def setMovie(self, new_movie):
        """
        Description: Setter to update a movie with new values
        :param new_movie: Movie
        :return: -
        """
        self.setTitle(new_movie.getTitle())
        self.setDescription(new_movie.getDescription())
        self.setType(new_movie.getType())

    def setTitle(self, new_title):
        """
        Description: Setter to update a movie's title with a new one
        :param new_title: string
        :return: -
        """
        self.__title = new_title

    def setDescription(self, new_description):
        """
        Description: Setter to update a movie's description with a new one
        :param new_description: string
        :return: -
        """
        self.__description = new_description

    def setType(self, new_type):
        """
        Description: Setter to update a movie's type with a new one
        :param new_type: string
        :return: -
        """
        self.__movie_type = new_type

    def __eq__(self, other):
        return (self.__title == other.__title and self.__movie_id == other.__movie_id
                and self.__movie_type == other.__movie_type and self.__description == other.__description)

    def __str__(self):
        return f"ID -> {self.__movie_id} TITLE: {self.__title} DESCRIPTION: {self.__description} TYPE: {self.__movie_type} \n"


class Client:
    """
    Description: Abstract data type for clients
    Domain: {id, name, CNP}
    """
    def __init__(self, client_id, name, cnp):
        self.__client_id = client_id
        self.__name = name
        self.__cnp = cnp

    def getId(self):
        """
        Description: Getter for the client's ID
        :return: string
        """
        return str(self.__client_id)

    def getName(self):
        """
        Description: Getter for the client's name
        :return: string
        """
        return self.__name

    def getCNP(self):
        """
        Description: Getter for the client's CNP
        :return: string
        """
        return self.__cnp

    def setId(self, new_id):
        """
        Description: Setter to update a client's ID with a new one
        :param new_id: string
        :return: -
        """
        self.__client_id = new_id

    def setName(self, new_name):
        """
        Description: Setter to update a client's name with a new one
        :param new_name: string
        :return: -
        """
        self.__name = new_name

    def setCNP(self, new_cnp):
        """
        Description: Setter to update a client's CNP with a new one
        :param new_cnp: string
        :return: -
        """
        self.__cnp = new_cnp

    def setClient(self, new_client):
        """
        Description: Setter to update a client with a new one
        :param new_client: Client
        :return: -
        """
        self.setName(new_client.getName())
        self.setCNP(new_client.getCNP())

    def __eq__(self, other):
        return self.__name == other.__name and self.__cnp == other.__cnp and self.__client_id == other.__client_id

    def __str__(self):
        return f"ID -> {self.__client_id} NAME: {self.__name} CNP: {self.__cnp} \n"


class RentDTO:
    """
    Description: Data Transfer Object used for raports
    Domain: {object, no_of_movies_rented}
    """
    def __init__(self, my_object, no_of_movies_rented):
        self.__object = my_object
        self.__no_of_movies_rented = no_of_movies_rented

    def getObject(self):
        """
        Description: Getter to get the object the DTO contains
        :param: -
        :return: Object (Client/Movie)
        """
        return self.__object

    def getNoOfRents(self):
        """
        Description: Getter to get the number of movies rented by the object
        :param: -
        :return: int
        """
        return self.__no_of_movies_rented

    def stringClient(self):
        return f"{self.__object.getName()} has rented {self.__no_of_movies_rented} movies.\n"

    def stringMovie(self):
        return f"{self.__object.getTitle()} / {self.__object.getType()}  has rented {self.__no_of_movies_rented} movies.\n"
