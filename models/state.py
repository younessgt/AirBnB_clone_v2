#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """ Method that return  the list of City instances
        with state_id equals to the current State.id"""
        from models import storage
        list_cities = [
            city_obj
            for city_obj in storage.all(City).values()
            if city_obj.state_id == self.id
        ]
        return list_cities
