#!/usr/bin/python3
"""
Module: models

Create amenity class (inherited from BaseModel)
"""
from models import base_model


class Amenity(base_model.BaseModel):
    """
    Create  amenity class

    Attributes:
    in addition to super attrs:
    name: (string) amenity name
    """

    name = ""
