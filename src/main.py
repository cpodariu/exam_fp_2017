from src.controller.SentenceController import SentenceController
from src.repository.SentenceRepo import SentenceRepository
from src.ui.console import Console

repo = SentenceRepository()
ctrl = SentenceController(repo)
cons = Console(ctrl)
cons.run()