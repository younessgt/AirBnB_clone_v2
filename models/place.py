#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column("place_id", String(60),
           ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60),
           ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")

    @property
    def reviews(self):
        """ Method that returns the list of Review instances
        with place_id equals to the current Place.id"""
        from models import storage
        list_reviews = [
            review_obj
            for review_obj in storage.all(Review).values()
            if review_obj.place_id == self.id
        ]
        return list_reviews

    @property
    def amenities(self):
        """ returns the list of Amenity instances based on
        the attribute amenity_ids that contains all Amenity.id """
        from models.amenity import Amenity
        from models import storage
        list_amenities = [
            amenity_obj
            for amenity_obj in storage.all(Amenity).values()
            if amenity_obj.id in self.amenity_ids
        ]
        return list_amenities

    @amenities.setter
    def amenities(self, obj=None):
        """ Handle the adding of the Amenity.id
        to the attribute amenity_ids"""
        if isinstance(obj, Amenity) and obj.id not in amenity_ids:
            self.amenity_ids.append(obj.id)
