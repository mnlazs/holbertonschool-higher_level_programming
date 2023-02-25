#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':
    username, password, database, state_name = argv[1:]

    # Creating the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Creating the session
    session = Session(engine)

    # Querying the database for the state
    query = session.query(State).filter(State.name == state_name).all()

    if query:
        # Printing the state id
        print(query[0].id)
    else:
        # Printing Not found if no state was found
        print('Not found')

    # Closing the session
    session.close()

