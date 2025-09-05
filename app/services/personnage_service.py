from sqlalchemy import text
from .db_tools import dbTools
from models.personnage import Personnage

class PersonnageService(dbTools):
	"""Classe représentant la logique de gestion des personnages"""

	def __init__(self,session):
		super().__init__(session)

	# Add => ORM
	def ajouter(self, nom, race):
		"""Ajoute un personnage avec méthode ORM"""
		perso = Personnage(nom=nom, race=race)
		self.session.add(perso)
		self.commit()
		return perso

	# Read one
	def chercher_par_id(self, id_):
		"""Recherche un personnage par son id"""
		return self.session.query(Personnage).filter_by(id=id_).first()

	# READ one(toutes les quêts / anneaux)  => ORM 
	def afficher_details(self, perso):
		"""Affiche les détails d'un personnage"""
		print(f"Nom : {perso.nom}")
		print(f"Race : {perso.race.nom}")
		# à complété avec d'autres tables....

	# Udptate => ORM
	def update_name(self, id, nouveau_nom):
		"""Modifie le nom d'un personnage"""
		p = self.chercher_par_id(id)
		if p:
			p.nom = nouveau_nom
			self.commit()

	# Delete => SQL BRUT
	def supprimer(self, id_):
		"""Supprimme un personnage via SQL BRUT"""
		self.session.execute(
			text("DELETE FROM personnage WHERE id = :{id}"),
			{"id": id_}
		)
		self.commit()
		print(f"Personnage id : {id_} supprimé !")
