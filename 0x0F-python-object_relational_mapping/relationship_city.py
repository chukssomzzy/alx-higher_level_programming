#!/usr/bin/python3
"""defines model for city"""

from sqlalchemy import Column, ForeignKey, Sequence, Integer, String
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """Defines a city model"""
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('city_id_seq'), primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    state = relationship("State", back_populates="cities")

    def __repr__(self):
        """represent the city instance"""
