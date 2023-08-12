#!/usr/bin/python3
"""
Module: models

Create state class (inherited from BaseModel)
"""
import base_model


class State(base_model.BaseModel):
    """
    Create  class state

    Attributes:
    in addition to super attrs:
    name: (string) state name
    """

    def __inti__(self):
        self.super().__init__()
        self.name = ""
