from repo import RepoInFile
from service import Service
from ui import UI

repo = RepoInFile("books.txt")
service = Service(repo)
console = UI(service)

console.run()