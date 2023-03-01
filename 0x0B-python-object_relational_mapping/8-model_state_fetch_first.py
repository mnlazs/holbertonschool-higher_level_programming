#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from model_state import Base, State


if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    url = URL.create(drivername= 'mysql+mysqldb', host= 'localhost',
                    username= mySQL_u, password= mySQL_p, database= db_name)

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)
    try:
        first = session.query(State).first()
        if first is not None:
            print("{}: {}".format(first.id, first.name))
        else:
            print("No se encontraron objetos State")
    except Exception as e:
            print('Error', e)
