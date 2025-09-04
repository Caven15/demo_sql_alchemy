from .base import Base
from sqlalchemy import Column, Integer, String

class Race(Base):
	__tablename__ = 'race'
	
	id = Column(Integer, primary_key=True)
	nom = Column(String, nullable=False)

