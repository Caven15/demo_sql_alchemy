from models.db.race import Race
from .db_tools import dbTools


class RaceService(dbTools):
    def __init__(self, session):
        # Initialise self.session depuis le dbTools
        super().__init__(session) 
    
    def peupler(self):
        """ Insère les races du seigneur des anneaux si la table est vide"""
        if self.session.query(Race).first():
            print("Les races existent déjà, aucun ajout !!")
            return
        
        races = [
			Race(nom="humain"),
			Race(nom="Elfe"),
			Race(nom="Nain"),
			Race(nom="Hobbit"),
			Race(nom="Orc"),
			Race(nom="ent")
		]
        
        self.session.add_all(races)
        self.commit()
    
    def lister(self):
        """Retourne toutes les Races en base """
        for race in self.session.query(Race).all():
            print(f"{race.id} - {race.nom}")