#!/usr/bin/python3
"""rdhjk rsthljksrt hklwjr htass."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Represents a city with SQLalchemy.

    Inherits from sqlalchemy.ext.declarative.Base.
    Links to the MySQL table cities.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
