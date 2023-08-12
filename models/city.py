#!/usr/bin/python3
"""
Module: models

Create city class (inherited from BaseModel)
"""
import base_model


class City(base_model.BaseModel):
    """
    Create city class

    Attributes:
    in addition to super attrs:
    state_id: (string) id of city state
    name: (string) city name
    """

    def __inti__(self):
        self.super().__init__()
        self.name = ""
        self.state_id = ""
