from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .personnage_quete import personnage_quete

class Quete(Base):
	__tablename__ = "quete"

	id = Column(Integer, primary_key=True)
	titre = Column(String, nullable=False)

	# Relation N:N avec personnages
	participants = relationship("Personnage", secondary=personnage_quete, back_populates="quetes")