#!/usr/bin/python3
"""Script that changes the name of a State object in the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == '__main__':
    username, password, database = argv[1:]

    # Creating the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Creating the session
    session = Session(engine)

    # Retrieving the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Updating the name of the state
    state.name = 'New Mexico'

    # Committing the transaction
    session.commit()

    # Closing the session
    session.close()
