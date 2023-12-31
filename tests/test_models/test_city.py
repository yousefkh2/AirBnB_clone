#!/usr/bin/python3
"""
Tests for models/city module(City)
"""

import unittest
from models.city import City
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.c1 = City()

    def test_inheritance(self):
        """Test if is inheriated from BaseModel"""
        self.assertIsInstance(self.c1, City)
        self.assertIsInstance(self.c1, BaseModel)

    def test_existing_attributes(self):
        """test if attributes is existing"""
        attr_lst = dir(self.c1)
        self.assertIn('name', attr_lst)
        self.assertIn("state_id", attr_lst)
        self.assertIn("id", attr_lst)
        self.assertIn("created_at", attr_lst)
        self.assertIn("updated_at", attr_lst)

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        self.assertIsInstance(self.c1.name, str)
        self.assertIsInstance(self.c1.state_id, str)
