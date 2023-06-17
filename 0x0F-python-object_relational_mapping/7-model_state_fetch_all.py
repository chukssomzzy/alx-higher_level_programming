#!/usr/bin/python3
"""List all state object from the database hbtn_0e_6_usa"""

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
            order_by(asc(State.id)).all():
        print(f"{id}: {name}")
