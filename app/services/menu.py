from .race_service import RaceService

class Menu:
    def __init__(self, session):
        self.session = session
        self.race = RaceService(session)
        self.race.peupler()
    
    def test(self):
        self.race.lister()