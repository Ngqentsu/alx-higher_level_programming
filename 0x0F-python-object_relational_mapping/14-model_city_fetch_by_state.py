#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_6_usa."""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_query = session.query(State.name).filter_by(id=city.state_id)
        state_name = state_query.first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()
