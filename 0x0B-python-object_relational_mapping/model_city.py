#!/usr/bin/python3
"""list all cities objects from the database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
 """Represents a state for a MySQL database.

    Args:
       __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
    """

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
