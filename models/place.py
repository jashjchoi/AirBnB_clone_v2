#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
storage_type = getenv('HBNB_TYPE_STORAGE')

""" instance of SQLAlchemy Table called place_amenity
for creating Many-To-Many relationship between Place and Amenity"""
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if storage_type == "db":
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
    else:
        @property
        def reviews(self):
            from models.review import Review
            from models import storage
            """
            getter attribute that returns the list of Review instances
            with place_id equals to the current Place.id
            """
            list_reviews = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            from models import Amenity
            from models import storage

            """
            Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place
            """
            list_amenities = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """
            Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids
            """
            from models import storage
            if type(value) == 'Amenity':
                self.amenitiy_ids.append(value.id)
