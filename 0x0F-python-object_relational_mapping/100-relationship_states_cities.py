#!/usr/bin/python3

"""Creates the State "California" with the City 'San Francisco'"""

import sys

from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    if new_state and new_city:
        new_state.cities.append(new_city)
        session.add(new_state)
        session.commit()
