#!/usr/bin/python3

"""lists all 'State' objects, and corresponding 'City' objects,
contained in the database"""

import sys

from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import asc, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    for state in session.query(State).join(City, State.cities).\
            order_by(asc(State.id), asc(City.id)).all():
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
