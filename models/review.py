#!/usr/bin/python3
"""
Module: models

Create review class (inherited from BaseModel)
"""
from models import base_model


class Review(base_model.BaseModel):
    """
    Create  a Reviews class

    Attributes:
    in addition to super attrs:
    place_id: (string) equals to Place.id
    user_id: (string) equals to User.id
    text: (string) represent review
    """

    place_id = ""
    user_id = ""
    text = ""
