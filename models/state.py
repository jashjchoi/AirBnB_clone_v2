#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade="all, delete",
                              backref='state')
    else:
        @property
        def cities(self):
            from models import storage
            """ getter attribute cities returns the list of City
                instances with state_id equals to the current State.id
            """
            list_cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                """Iterate through all cities and if the
                city.state_id is eqaul to the current state id
                add it to the list to be returned"""
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
