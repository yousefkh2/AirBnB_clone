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

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
