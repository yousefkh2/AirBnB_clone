#!/usr/bin/python3
"""
Module: models

Create user class (inherited from BaseModel)
"""
import base_model


class User(base_model.BaseModel):
    """
    web User class

    attributes:
        Addition to super attributes the following attrs:
        email: (string) user emai address
        password: (string) user password
        first_name: (string) user first name
        last_name: (string) user last name
    """

    def __inti__(self):
        self.super().__inti__()
        self.email = ""
        self.passowrd = ""
        self.first_name = ""
        self.last_name = ""
