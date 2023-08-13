#!/usr/bin/python3
"""
Module: models

Create city class (inherited from BaseModel)
"""
from models import base_model


class City(base_model.BaseModel):
    """
    Create city class

    Attributes:
    in addition to super attrs:
    state_id: (string) id of city state
    name: (string) city name
    """

    name = ""
    state_id = ""
