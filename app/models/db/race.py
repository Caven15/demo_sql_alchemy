from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Race(Base):
	__tablename__ = 'race'
	
	id = Column(Integer, primary_key=True)
	nom = Column(String, nullable=False)

	personnage = relationship("Personnage", back_populates="race")