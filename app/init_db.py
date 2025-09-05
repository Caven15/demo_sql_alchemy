from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


# import des modèles
from config import URL_DB
from models.base import Base
from models import race, personnage, anneau, quete, personnage_quete

engine = None
session = None
db_connected = False

try:
    # Connexion à la base de donnée
    engine = create_engine(URL_DB)
    
    # Initialisation de la session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Suppresion des tables
    Base.metadata.drop_all(bind=engine)
    
    # Création des tables si elles n'existent pas
    Base.metadata.create_all(bind=engine)
    
    db_connected = True
    print("--------------------------")
    print("Connexion DB + modèles créer !!!")
    print("--------------------------")
except SQLAlchemyError as error:
    print("Erreur lors de la connexion à la base donnée :")
    print(error)