#!/usr/bin/python3

"""prints all city objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, id, city in session.query(State.name, City.id, City.name).\
            join(City, State.id == City.state_id).all():
        print(state, id, city)
