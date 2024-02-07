from repository import RepositoryFile
from service import Service
from validators import Validator
from ui import Ui

repo = RepositoryFile("exams.txt")
validator = Validator()
service = Service(repo, validator)
ui = Ui(service)

ui.run()

