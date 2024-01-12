import unittest
from repository.movie_repo import MovieRepositoryInMemory
from repository.client_repo import ClientRepositoryInMemory
from repository.rent_repo import RentRepositoryInMemory
from domain.entities import Client, Movie
from domain.validators import ClientValidator, MovieValidator
from service.service_movie import MovieService
from service.service_client import ClientService
from service.service_rent import RentService
import random
import string


# DOMAIN & VALIDATOR TESTS ---------------------------------


class testClient(unittest.TestCase):
    def test_create_client(self):
        person = Client(1000, "Dan Gaspar", "5040812339573")

        self.assertEqual(person.getId(), "1000")
        self.assertEqual(person.getName(), "Dan Gaspar")
        self.assertEqual(person.getCNP(), "5040812339573")

        person.setCNP("6060517339814")
        person.setName("Stanca Norina")

        self.assertEqual(person.getName(), "Stanca Norina")
        self.assertEqual(person.getCNP(), "6060517339814")

    def test_equal_clients(self):
        person_one = Client(1000, "Dan Gaspar", "5040812339573")
        person_two = Client(1000, "Dan Gaspar", "5040812339573")
        person_three = Client(1000, "Gabriel Gaspar", "5040812339573")

        self.assertEqual(person_one, person_two)
        self.assertNotEqual(person_one, person_three)

    def test_validate_client(self):
        valid_person = Client(1000, "Dan Gaspar", "5040812339573")
        invalid_person = Client(1000, "", "")
        invalid_cnp_person = Client(1000, "Dan Gaspar", "6060517339813")

        validator = ClientValidator()

        self.assertRaises(ValueError, validator.validate, invalid_person)
        # try:
        #     validator.validate(valid_person)
        #     assert True
        # except ValueError:
        #     assert False

        self.assertRaises(ValueError, validator.validate, invalid_person)
        try:
            validator.validate(invalid_person)
            assert False
        except ValueError as ve:
            self.assertEqual(str(ve), "The name cannot be empty.\nThe CNP cannot be empty.\n")

        try:
            validator.validate(invalid_cnp_person)
            assert False
        except ValueError as ve:
            self.assertEqual(str(ve), "The CNP is invalid numeric - last digit is invalid.\n")


class testMovie(unittest.TestCase):
    def test_create_movie(self):
        film = Movie(1000, "TENET", "A spy tries to stop a future war", "Spy")
        self.assertEqual(film.getTitle(), "TENET")
        self.assertEqual(film.getDescription(), "A spy tries to stop a future war")
        self.assertEqual(film.getId(), '1000')
        self.assertEqual(film.getType(), "Spy")

        film.setType("Law")
        film.setTitle("Suits")
        film.setDescription("A fraud is the best lawyer in New York")

        self.assertEqual(film.getTitle(), "Suits")
        self.assertEqual(film.getDescription(), "A fraud is the best lawyer in New York")
        self.assertEqual(film.getType(), "Law")

    def test_equal_movies(self):
        film_one = Movie(1000, "TENET", "A spy tries to stop a future war", "Spy")
        film_two = Movie(1000, "TENET", "A spy tries to stop a future war", "Spy")
        film_three = Movie(1001, "Suits", "A fraud is the best lawyer in New York", "Law")

        self.assertEqual(film_one, film_two)
        self.assertNotEqual(film_one, film_three)

    def test_validate_movie(self):
        valid_movie = Movie(1000, "TENET", "A spy tries to stop a future war", "Spy")
        invalid_movie = Movie(1, "", "", "")
        validator = MovieValidator()
        validator.validate(valid_movie)
        self.assertRaises(ValueError, validator.validate, invalid_movie)
        try:
            validator.validate(invalid_movie)
            assert False
        except ValueError as ve:
            self.assertEqual(str(ve),
                             "The title cannot be empty.\nThe description cannot be empty.\nThe type cannot be empty.\n")


# REPOSITORY TESTS ------------------------------------------


class testMovieRepo(unittest.TestCase):
    def setUp(self):
        self.__repo1 = MovieRepositoryInMemory()
        self.__repo2 = MovieRepositoryInMemory()

    def test_add_repo(self):
        movie1 = Movie(1, "TENET", "Awesome", "Spy")
        movie2 = Movie(2, "Law", "Suits", "Action")
        self.__repo1.add_movie(movie1)
        self.__repo1.add_movie(movie2)

        self.assertNotEqual(movie1, movie2)
        self.assertEqual(len(self.__repo1.get_all_movies()), 2)

        movies = self.__repo1.get_all_movies()
        self.assertNotEqual(movies[0], movies[1])

        try:
            self.__repo1.add_movie(movie1)
            assert False
        except Exception as ex:
            self.assertEqual(str(ex), "The ID already exists!\n")

    def test_delete_repo(self):
        movie1 = Movie(1, "TENET", "Awesome", "Spy")
        self.__repo1.add_movie(movie1)

        self.__repo1.delete_movie("1")
        self.assertEqual(len(self.__repo1.get_all_movies()), 0)

        self.__repo1.add_movie(movie1)

        try:
            self.__repo1.delete_movie(2)
            assert False
        except Exception as ex:
            self.assertEqual(str(ex), "The ID does not exist!\n")

    def test_update_repo(self):
        movie1 = Movie(1, "TENET", "Awesome", "Spy")
        self.__repo1.add_movie(movie1)
        movie2 = Movie(1, "Suits", "Cool", "Law")
        self.__repo1.update_movie("1", movie2)

        self.assertEqual(self.__repo1.get_movie("1"), movie2)


class testClientRepo(unittest.TestCase):

    def setUp(self):
        self.__repo1 = ClientRepositoryInMemory()
        self.__repo2 = ClientRepositoryInMemory()

    def test_add_repo(self):
        client1 = Client(1, "Dan", "5040812339573")
        client2 = Client(2, "Norina", "6051706330209")
        self.__repo1.add_client(client1)
        self.__repo1.add_client(client2)

        self.assertEqual(len(self.__repo1.get_all_clients()), 2)

        self.assertRaises(Exception, self.__repo1.add_client, client1)

        # try:
        #     self.__repo1.add_client(client1)
        #     assert False
        # except Exception as ex:
        #     self.assertEqual(str(ex), "The ID already exists!\n")

    def test_delete_repo(self):
        client1 = Client(1, "Dan", "5040812339573")
        self.__repo1.add_client(client1)

        self.__repo1.delete_client("1")
        self.assertEqual(len(self.__repo1.get_all_clients()), 0)

        self.__repo1.add_client(client1)

        self.assertRaises(Exception, self.__repo1.delete_client, "2")

        # try:
        #     self.__repo1.delete_client("2")
        #     assert False
        # except Exception as ex:
        #     self.assertEqual(str(ex), "The ID does not exist!\n")

    def test_update_repo(self):
        client1 = Client(1, "Dan", "5040812339573")
        self.__repo1.add_client(client1)
        client2 = Client(1, "Norina", "6051706330209")
        self.__repo1.update_client("1", client2)

        self.assertEqual(self.__repo1.get_client("1"), client2)


# SERVICE TESTS --------------------------------------------


class testMovieService(unittest.TestCase):
    def setUp(self):
        self.__repo = MovieRepositoryInMemory()
        self.__validator = MovieValidator()
        self.__srv = MovieService(self.__repo, self.__validator)

    def test_add_random_movie(self):
        self.__srv.add_random_movie(1, 10)
        self.assertEqual(len(self.__repo.get_all_movies()), 1)

        test_movie = self.__repo.get_movie("1")
        random.seed(10)
        test_title = ''.join(random.choices(string.ascii_lowercase, k=7))
        random.seed(10)
        test_description = ''.join(random.choices(string.ascii_lowercase, k=10))
        random.seed(10)
        test_movie_type = ''.join(random.choices(string.ascii_lowercase, k=6))
        test_film = Movie(1, test_title, test_description, test_movie_type)
        self.assertEqual(test_movie, test_film)

    def test_create_and_add_movie(self):
        self.__srv.create_movie_and_add_it("1", "Suits", "Law", "Action")
        self.__srv.create_movie_and_add_it("2", "TENET", "Cool", "Spy")
        self.assertEqual(len(self.__repo.get_all_movies()), 2)
        self.assertEqual(self.__repo.get_movie("1").getTitle(), "Suits")
        self.assertEqual(self.__repo.get_movie("1").getDescription(), "Law")
        self.assertEqual(self.__repo.get_movie("1").getType(), "Action")

    def test_update_movie(self):
        self.__srv.create_movie_and_add_it("1", "Suits", "Law", "Action")
        self.__srv.update_movie_by_id("1", "TENET", "Cool", "Spy")
        self.assertEqual(len(self.__repo.get_all_movies()), 1)
        self.assertEqual(self.__repo.get_movie("1").getTitle(), "TENET")
        self.assertEqual(self.__repo.get_movie("1").getDescription(), "Cool")
        self.assertEqual(self.__repo.get_movie("1").getType(), "Spy")

    def test_print_all_movies(self):
        self.__srv.create_movie_and_add_it("1", "Suits", "Law", "Action")
        self.__srv.create_movie_and_add_it("2", "TENET", "Cool", "Spy")
        test_string = ("ID -> 1 TITLE: Suits DESCRIPTION: Law TYPE: Action \n"
                       "ID -> 2 TITLE: TENET DESCRIPTION: Cool TYPE: Spy \n")

        self.assertEqual(self.__srv.print_all_movies(), test_string)

    def test_search_movie_by_title(self):
        self.__srv.create_movie_and_add_it("1", "Suits", "Law", "Action")
        self.__srv.create_movie_and_add_it("2", "TENET", "Cool", "Spy")
        test_string = "ID -> 2 TITLE: TENET DESCRIPTION: Cool TYPE: Spy \n"
        self.assertEqual(self.__srv.search_movie_by_title("TENET"), test_string)
        test_string = "ID -> 1 TITLE: Suits DESCRIPTION: Law TYPE: Action \n"
        self.assertEqual(self.__srv.search_movie_by_title("Suits"), test_string)

    def test_get_movie_by_id(self):
        self.__srv.create_movie_and_add_it("1", "Suits", "Law", "Action")
        self.__srv.create_movie_and_add_it("2", "TENET", "Cool", "Spy")
        test_movie = Movie("1", "Suits", "Law", "Action")
        test_second_movie = Movie("2", "TENET", "Cool", "Spy")
        self.assertEqual(self.__srv.get_movie_by_id("1"), test_movie)
        self.assertEqual(self.__srv.get_movie_by_id("2"), test_second_movie)


class testClientService(unittest.TestCase):
    def setUp(self):
        self.__repo = ClientRepositoryInMemory()
        self.__validator = ClientValidator()
        self.__srv = ClientService(self.__repo, self.__validator)

    def test_add_random_client(self):
        """
        This won't work due to the fact that it will not generate a random Romanian Valid CNP
        """

        # self.__srv.add_random_client(1, 10)
        self.assertEqual(len(self.__repo.get_all_clients()), 0)

        """
        test_client = self.__repo.get_client("1")
        random.seed(10)
        test_name = ''.join(random.choices(string.ascii_lowercase, k=7))
        random.seed(10)
        test_cnp = str(random.randint(1000000000000, 9999999999999))
        test_person = client(1, test_name, test_cnp)
        self.assertEqual(test_person, test_client)
        """

    def test_create_client_and_add_it(self):
        self.__srv.create_client_and_add_it("1", "Dan", "5040812339573")
        self.__srv.create_client_and_add_it("2", "Mihai", "1990524335411")
        self.assertEqual(len(self.__repo.get_all_clients()), 2)
        self.assertEqual(self.__srv.get_client_by_id("1").getId(), "1")
        self.assertEqual(self.__srv.get_client_by_id("2").getName(), "Mihai")
        self.assertEqual(self.__srv.get_client_by_id("1").getCNP(), "5040812339573")

    def test_update_client(self):
        self.__srv.create_client_and_add_it("2", "Dan", "5040812339573")
        self.__srv.update_client_by_id("2", "Mihai", "1990524335411")
        self.assertEqual(self.__repo.get_client("2").getName(), "Mihai")
        self.assertEqual(self.__repo.get_client("2").getCNP(), "1990524335411")

    def test_print_all_clients(self):
        self.__srv.create_client_and_add_it("1", "Dan", "5040812339573")
        self.__srv.create_client_and_add_it("2", "Mihai", "1990524335411")
        test_string = ("ID -> 1 NAME: Dan CNP: 5040812339573 \n"
                       "ID -> 2 NAME: Mihai CNP: 1990524335411 \n")

        self.assertEqual(self.__srv.print_all_clients(), test_string)

    def test_search_client_by_name(self):
        self.__srv.create_client_and_add_it("1", "Dan", "5040812339573")
        self.__srv.create_client_and_add_it("2", "Mihai", "1990524335411")
        test_string = "ID -> 1 NAME: Dan CNP: 5040812339573 \n"
        self.assertEqual(self.__srv.search_client_by_name("Dan"), test_string)
        test_string = "ID -> 2 NAME: Mihai CNP: 1990524335411 \n"
        self.assertEqual(self.__srv.search_client_by_name("Mihai"), test_string)

    def test_get_client_by_id(self):
        self.__srv.create_client_and_add_it("1", "Dan", "5040812339573")
        self.__srv.create_client_and_add_it("2", "Mihai", "1990524335411")
        test_client = Client("1", "Dan", "5040812339573")
        self.assertEqual(self.__srv.get_client_by_id("1"), test_client)

    def test_get_all_clients_list(self):
        self.__srv.create_client_and_add_it("1", "Dan", "5040812339573")
        self.__srv.create_client_and_add_it("2", "Mihai", "1990524335411")
        self.assertEqual(len(self.__srv.get_all_clients_list()), 2)

# RENT TESTS ----------------------------------------------


class testRent(unittest.TestCase):
    def setUp(self):
        self.__repo_clients = ClientRepositoryInMemory()
        self.__validator_clients = ClientValidator()
        self.__srv_clients = ClientService(self.__repo_clients, self.__validator_clients)
        self.__repo_movies = MovieRepositoryInMemory()
        self.__validator_movies = MovieValidator()
        self.__srv_movies = MovieService(self.__repo_movies, self.__validator_movies)
        self.__repo_rent = RentRepositoryInMemory()
        self.__srv_rent = RentService(self.__repo_movies, self.__repo_clients, self.__repo_rent)

    def test_rent_a_movie(self):
        film = Movie("1", "TENET", "A spy tries to stop a future war", "Spy")
        person = Client("1", "Dan Gaspar", "5040812339573")
        self.__srv_rent.rent_a_movie_by_a_client(film, person)
        self.assertEqual(len(self.__repo_rent.get_all_rents_by_list_of_objets()), 1)
        rent = self.__repo_rent.get_all_rents_by_a_client(person)
        self.assertEqual(rent[0][0], person)
        self.assertEqual(rent[0][1], film)
        self.assertEqual(rent[0][2], True)

    def test_return_a_movie(self):
        film = Movie("1", "TENET", "A spy tries to stop a future war", "Spy")
        person = Client("1", "Dan Gaspar", "5040812339573")
        self.__srv_rent.rent_a_movie_by_a_client(film, person)
        self.__srv_rent.return_a_movie_by_a_client(film, person)
        rents = self.__srv_rent.get_all_rents_by_list_of_objects()
        self.assertEqual(rents[0][2], False)

    def test_get_all_rents_as_a_string(self):
        film = Movie("1", "TENET", "A spy tries to stop a future war", "Spy")
        film_two = Movie("2", "Suits", "Fraud", "Law")
        person = Client("1", "Dan Gaspar", "5040812339573")

        self.__srv_rent.rent_a_movie_by_a_client(film, person)
        self.__srv_rent.rent_a_movie_by_a_client(film_two, person)
        test_string = ("Client: Dan Gaspar (ID: 1) | Movie Rented: TENET (ID: 1)\n"
                       "Client: Dan Gaspar (ID: 1) | Movie Rented: Suits (ID: 2)\n")
        self.assertEqual(self.__srv_rent.get_all_rents_as_string(), test_string)


if __name__ == "__main__":
    unittest.main()
