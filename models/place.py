#!/usr/bin/python3
"""
Module: models

Create place class (inherited from BaseModel)
"""
from models import base_model


class Place(base_model.BaseModel):
    """
    Create place class

    Attributes:
    in addition to super attrs:
    name: (string) state name
    city_id: (string) id of palce city
    user_id: (string) id of user
    description: (string)
    number_rooms: (Integer)
    number_bathrooms: (Integer)
    max_guest: (Integer)
    price_by_night: (Integer)
    latitude: (Float)
    longitude: (float)
    amenity_ids: (list of strings) 
    """

    def __inti__(self):
        self.super().__init__()
        self.name = ""
        self.city_id = ""
        self.user_id = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        
