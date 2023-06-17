#!/usr/bin/python3
"""python file that contains the class definition of a state and an instance
Base = declarative_base
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Sequence, Column, Integer, String

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(name=%s)>" % self.name
