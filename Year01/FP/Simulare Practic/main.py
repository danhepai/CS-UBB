from ui import ConsoleUI
from service import Service
from repository import RepoConcurenti, RepoParticipare

repo_con = RepoConcurenti("concurenti.txt")
repo_par = RepoParticipare("participari.txt")
my_service = Service(repo_con, repo_par)

my_ui = ConsoleUI(my_service)

my_ui.run()
