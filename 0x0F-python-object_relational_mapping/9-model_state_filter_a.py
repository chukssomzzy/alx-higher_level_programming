#!/usr/bin/python3

"""Lists all state objects that contains the letter a from the database """

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
    for id, name in session.query(State.id, State.name).\
            filter(State.name.like("%a%")).\
            order_by(asc(State.id)).all():
        print(f"{id}: {name}")
