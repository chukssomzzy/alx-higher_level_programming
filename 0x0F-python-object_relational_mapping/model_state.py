#!/usr/bin/python3

"""contains the class definition of a state and an instance Base =
declarative()"""
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base();
engine = create_engine(
    f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{[3]}")

class
