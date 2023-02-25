#!/usr/bin/python3
"""Script that adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""

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

    # Creating the new state
    new_state = State(name='Louisiana')

    # Adding the new state to the session
    session.add(new_state)

    # Committing the transaction
    session.commit()

    # Printing the new state id
    print(new_state.id)

    # Closing the session
    session.close()
