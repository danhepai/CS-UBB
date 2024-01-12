from userinterface.ui import ConsoleUI
from service.service_movie import MovieService
from service.service_client import ClientService
from service.service_rent import RentService
from repository.movie_repo import MovieRepositoryInMemory, MovieRepositoryFile
from repository.client_repo import ClientRepositoryInMemory, ClientRepositoryFile, ClientRepositoryFileSecondary
from repository.rent_repo import RentRepositoryInMemory, RentRepositoryFile
from domain.validators import MovieValidator, ClientValidator

repo_movies = MovieRepositoryFile("data/movies.txt")
# repo_movies = MovieRepositoryInMemory()
valid_movie = MovieValidator()
# repo_clients = ClientRepositoryInMemory()
repo_clients = ClientRepositoryFileSecondary("data/clients_secondary.txt")
valid_client = ClientValidator()
# repo_rents = RentRepository()
repo_rents = RentRepositoryFile("data/rents.txt")

movie_srv = MovieService(repo_movies, valid_movie)
client_srv = ClientService(repo_clients, valid_client)
rent_srv = RentService(repo_movies, repo_clients, repo_rents)

ui = ConsoleUI(movie_srv, client_srv, rent_srv)

ui.run()
