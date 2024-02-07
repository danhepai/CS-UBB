from console import ConsoleUi
from service import Service
from repo import RepoInFile
from validators import Validator

file = "tractors.txt"
repo = RepoInFile(file)
validator = Validator()
srv = Service(repo, validator)
ui = ConsoleUi(srv)

ui.run()
