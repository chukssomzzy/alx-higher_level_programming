#!/usr/bin/python3

"""Prints the state object with the name passed
as argument from the database"""

import sys
from model_state import Base, State

from sqlalchemy import asc, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state_id = session.query(State.id).filter_by(name=sys.argv[4]).first()
    if state_id:
        print(state_id[0])
    else:
        print("Not found")
