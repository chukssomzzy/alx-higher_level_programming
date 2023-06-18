#!/usr/bin/python3
"""python file that contains the class definition of a state and an instance
Base = declarative_base
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Sequence, Column, Integer, String

Base = declarative_base()


class State(Base):
    """Defines a model for state"""
    __tablename__ = 'states'
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete, delete-orphan")

    def __repr__(self):
        """represents a state instance"""
        return "<State(name=%s)>" % self.name
