#!/usr/bin/python3
"""
Tests for models/amenity module(Amenity)
"""

import unittest
from models.amenity import Amenity
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.c1 = Amenity()

    def test_inheritance(self):
        """Test if is inheriated from BaseModel"""
        self.assertIsInstance(self.c1, Amenity)
        self.assertIsInstance(self.c1, BaseModel)

    def test_existing_attributes(self):
        """test if attributes is existing"""
        attr_lst = dir(self.c1)
        self.assertIn('name', attr_lst)
        self.assertIn("id", attr_lst)
        self.assertIn("created_at", attr_lst)
        self.assertIn("updated_at", attr_lst)

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        self.assertIsInstance(self.c1.name, str)
