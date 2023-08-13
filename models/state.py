#!/usr/bin/python3
"""
Module: models

Create state class (inherited from BaseModel)
"""
from models import base_model


class State(base_model.BaseModel):
    """
    Create  class state

    Attributes:
    in addition to super attrs:
    name: (string) state name
    """

    name = ""
