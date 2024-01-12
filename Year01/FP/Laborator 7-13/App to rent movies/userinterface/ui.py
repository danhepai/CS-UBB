from utils.id_utils import generate_id


def menu():
    print("This is your app to manage clients & movies. Input an option from below:")
    print("1. Commands to manage clients & movies.")
    print(
        "Options available: ADD Client/Movie, DELETE Client/Movie, UPDATE Client/Movie, SEARCH Client/Movie, PRINT Clients/Movies")
    print("2. Commands for renting")
    print("Options available: RENT a Movie, RETURN a Movie")
    print("3. Commands to print raports.")
    print("Options available: clients with rents, most rented movies, 30% clients with most rents")
    print("4. 'EXIT' COMMAND FOR QUITING APP")


class ConsoleUI:
    def __init__(self, service_movie, service_client, service_rent):
        self.__service_movie = service_movie
        self.__service_client = service_client
        self.__service_rent = service_rent
        self.__commands = {"add movie": self.__ui_add_movie,
                           "add client": self.__ui_add_client,
                           "delete movie": self.__ui_delete_movie,
                           "delete client": self.__ui_delete_client,
                           "update movie": self.__ui_update_movie,
                           "update client": self.__ui_update_client,
                           "search movie": self.__ui_search_movie,
                           "search client": self.__ui_search_client,
                           "print movies": self.__ui_print_all_movies,
                           "print clients": self.__ui_print_all_clients,
                           "add random client": self.__ui_add_random_client,
                           "add random movie": self.__ui_add_random_movie,
                           "rent a movie": self.__ui_rent_a_movie,
                           "return a movie": self.__ui_return_a_movie,
                           "print rents": self.__ui_print_all_rents,
                           "clients with rents": self.__ui_clients_with_rents,
                           "most rented movies": self.__ui_most_rented_movies,
                           "30% clients with most rents": self.__ui_30_percent_clients_with_most_rents}

    # ------------------------------------------------------------------ MOVIE ZONE:

    def __ui_add_random_movie(self):
        self.__service_movie.add_random_movie(str(generate_id(self.__service_movie.get_all_movies_list())))

    def __ui_update_movie(self):
        print("The movies that can be updated are:")
        print(self.__service_movie.print_all_movies())
        end = True
        while end:
            id_to_update = str(input("Introduce the id you want to update: "))
            new_title = input("Movie's new title: ")
            new_desc = input("Movie's new description: ")
            new_typ = input("Movie's new type: ")
            try:
                self.__service_movie.update_movie_by_id(id_to_update, new_title, new_desc, new_typ)
                print("Movie updated!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_print_all_movies(self):
        print(self.__service_movie.print_all_movies())

    def __ui_add_movie(self):
        end = True
        while end:
            title = input("Movie's title: ")
            desc = input("Movie's description: ")
            typ = input("Movie's type: ")
            try:
                self.__service_movie.create_movie_and_add_it(
                    str(generate_id(self.__service_movie.get_all_movies_list())), title, desc, typ)
                print("Movie added!")
                end = False
            except ValueError as ve:
                print(ve)

    def __ui_search_movie(self):
        title = input("Introduce the title of the movie you want to search: ")
        movies_found = self.__service_movie.search_movie_by_title(title)
        if movies_found == "":
            print("No movie with this title available")
        else:
            print("Movies found are:\n")
            print(movies_found)

    # ------------------------------------------------------------------ CLIENT ZONE:

    def __ui_add_random_client(self):
        self.__service_client.add_random_client(str(generate_id(self.__service_client.get_all_clients_list())))

    def __ui_search_client(self):
        name = input("Introduce the name of the client you want to search: ")
        clients_found = self.__service_client.search_client_by_name(name)
        if clients_found == "":
            print("No clients with this name available")
        else:
            print("Clients found are:\n")
            print(clients_found)

    def __ui_update_client(self):
        print("The clients that can be updated:")
        print(self.__service_client.print_all_clients())
        end = True
        while end:
            id_to_update = input("Introduce the id you want to update: ")
            new_name = input("Client's new name: ")
            new_CNP = input("Client's new CNP: ")
            try:
                self.__service_client.update_client_by_id(id_to_update, new_name, new_CNP)
                print("Client updated!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_add_client(self):
        end = True
        while end:
            name = input("Client's name: ")
            CNP = input("Client's cnp: ")
            try:
                self.__service_client.create_client_and_add_it(
                    str(generate_id(self.__service_client.get_all_clients_list())), name, CNP)
                print("Client added!")
                end = False
            except ValueError as ve:
                print(ve)

    def __ui_print_all_clients(self):
        print(self.__service_client.print_all_clients())

    # ------------------------------------------------------------------ RENT ZONE:

    def __ui_delete_movie(self):
        print(self.__service_movie.print_all_movies())
        end = True
        while end:
            id_to_delete = input("Introduce the id you want to delete: ")
            try:
                self.__service_rent.delete_movie_by_id(id_to_delete)
                print("Movie deleted!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_delete_client(self):
        print(self.__service_client.print_all_clients())
        end = True
        while end:
            id_to_delete = input("Introduce the id you want to delete: ")
            try:
                self.__service_rent.delete_client_by_id(id_to_delete)
                print("Client deleted!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_rent_a_movie(self):
        print("The clients that can rent a movie are:")
        print(self.__service_client.print_all_clients())
        print("The movies that can be rented are:")
        print(self.__service_movie.print_all_movies())
        end = True
        while end:
            id_client = input("Introduce the ID for the client: ")
            id_movie = input("Introduce the ID for the movie: ")
            try:
                movie_to_rent = self.__service_movie.get_movie_by_id(id_movie)
                person_that_rents = self.__service_client.get_client_by_id(id_client)
                self.__service_rent.rent_a_movie_by_a_client(movie_to_rent, person_that_rents)
                print("Movie rented!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_return_a_movie(self):
        print(self.__service_rent.get_all_rents_as_string())
        end = True
        while end:
            id_client = input("Introduce the ID for the client: ")
            id_movie = input("Introduce the ID for the movie: ")
            try:
                movie_to_return = self.__service_movie.get_movie_by_id(id_movie)
                person_that_returns = self.__service_client.get_client_by_id(id_client)
                self.__service_rent.return_a_movie_by_a_client(movie_to_return, person_that_returns)
                print("Movie returned!")
                end = False
            except Exception as ex:
                print(ex)

    def __ui_print_all_rents(self):
        print(self.__service_rent.get_all_rents_as_string())

    def __ui_clients_with_rents(self):
        end = True
        while end:
            cmd = input("You want them order by name or by the numbers of movies rented? Options: name/movies\n>>> ")
            if cmd == "name":
                try:
                    print(self.__service_rent.get_rents_sorted_by_name())
                except Exception as ex:
                    print(ex)
                end = False
            elif cmd == "movies":
                try:
                    print(self.__service_rent.get_rents_sorted_by_number_of_movies_rented())
                except Exception as ex:
                    print(ex)
                end = False
            else:
                print("Invalid option.")

    def __ui_most_rented_movies(self):
        try:
            print(self.__service_rent.get_most_rented_movies())
        except Exception as ex:
            print(ex)

    def __ui_30_percent_clients_with_most_rents(self):
        try:
            print(self.__service_rent.get_30_percent_clients_with_most_rents())
        except Exception as ex:
            print(ex)
    # ------------------------------------------------------------------ MAIN MENU:

    def run(self):
        menu()
        while True:
            cmd = input(">>> ").strip().lower()
            if cmd == "exit" or cmd == "quit":
                return

            if cmd in self.__commands:
                try:
                    self.__commands[cmd]()
                except Exception as ex:
                    print(ex)
            else:
                print("Your menu command is invalid.")
