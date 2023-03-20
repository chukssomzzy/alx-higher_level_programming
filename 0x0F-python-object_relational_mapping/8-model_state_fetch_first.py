#!/usr/bin/python3

"""Prints the first state object from the databae hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    firstRow = session.query(State.id, State.name).order_by(State.id).first()
    if firstRow:
        print(f"{firstRow.id}: {firstRow.name}")
    else:
        print("Nothing")