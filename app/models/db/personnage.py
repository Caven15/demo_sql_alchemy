from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Personnage(Base):
    __tablename__ = 'personnage'
    
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    
    # FK vers Race
    race_id = Column(Integer, ForeignKey("race.id"))
    race = relationship("Race", back_populates="personnage")