from models.race import Race
from .race_service import RaceService
from .personnage_service import PersonnageService

class Menu:
    def __init__(self, session):
        self.session = session
        self.race = RaceService(session)
        self.personnage = PersonnageService(session)
        self.race.peupler()
    
    def test(self):
        race_id = int(input("Id de la race "))
        race = self.session.query(Race).filter_by(id=race_id).first()
        perso = self.personnage.ajouter("Bilbon",race)
        type(perso)
        if perso is not None:
            print(f"Personnage ajouté avec succès !!!")