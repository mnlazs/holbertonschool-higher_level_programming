#!/usr/bin/python3
#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # create connection to the database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query all City objects and print their information
    for city, state in session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # close the session
    session.close()
