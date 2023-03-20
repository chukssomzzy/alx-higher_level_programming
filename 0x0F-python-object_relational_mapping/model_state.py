#!/usr/bin/python3

"""contains the class definition of a state and an instance Base =
declarative()"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_city import City

Base = declarative_base()


class State(Base):
    """Defines a base class states"""

    __tablename__ = "states"
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)


State.cities = relationship(
    "City", order_by=City.id, back_populates="state")
