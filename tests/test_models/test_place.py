#!/usr/bin/python3
"""
Tests for models/place module(Place)
"""

import unittest
from models.place import Place
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.c1 = Place()

    def test_inheritance(self):
        """Test if is inheriated from BaseModel"""
        self.assertIsInstance(self.c1, Place)
        self.assertIsInstance(self.c1, BaseModel)

    def test_existing_attributes(self):
        """test if attributes is existing"""
        attr_lst = dir(self.c1)
        valid_attr = ["name", "city_id", "user_id", "description",
                      "number_rooms", "number_bathrooms", "max_guest",
                      "price_by_night", "latitude", "longitude", "amenity_ids",
                      "id", "created_at", "updated_at"]
        for attrs in valid_attr:
            self.assertIn(attrs, attr_lst)

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        valid_attr = ["name", "city_id", "user_id", "description",
                      "number_rooms", "number_bathrooms", "max_guest",
                      "price_by_night", "latitude", "longitude", "amenity_ids",
                      "id", "created_at", "updated_at"]
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.city_id, str)
        self.assertIsInstance(self.c1.user_id, str)
        self.assertIsInstance(self.c1.description, str)
        self.assertIsInstance(self.c1.number_rooms, int)
        self.assertIsInstance(self.c1.number_bathrooms, int)
        self.assertIsInstance(self.c1.max_guest, int)
        self.assertIsInstance(self.c1.price_by_night, int)
        self.assertIsInstance(self.c1.latitude, float)
        self.assertIsInstance(self.c1.longitude, float)
        self.assertIsInstance(self.c1.amenity_ids, list)
