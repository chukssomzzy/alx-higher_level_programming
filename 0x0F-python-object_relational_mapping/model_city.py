#!/usr/bin/python3
"""Contains the class definition of a city"""
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """class definition of City"""

    __tablename__ = "cities"
    id = Column(Integer, Sequence('city_id_sq'), primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
