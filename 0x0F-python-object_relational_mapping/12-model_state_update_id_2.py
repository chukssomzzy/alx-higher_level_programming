#!/usr/bin/python3
"""changes the name of a state object from the database """

import sys

from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    up_state = session.query(State).filter_by(id=2).first()
    if up_state:
        up_state.name = "New Mexico"
        session.commit()
