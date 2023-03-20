#!/usr/bin/python3
"""Contains the class definition of a city"""
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, Sequence('city_id_sq'), primary_key=True)
    name = Column(String(128))
    stat
