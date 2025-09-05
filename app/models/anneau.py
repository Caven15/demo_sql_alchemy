from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Anneau(Base):
	__tablename__ = 'anneau'

	id = Column(Integer, primary_key=True)
	nom = Column(String, nullable=False)

	# lien 1:1 avec personnage
	proprietaire_id = Column(Integer, ForeignKey("personnage.id"))
	proprietaire = relationship("Personnage", back_populates="anneau")