#!/usr/bin/python3
"""
Tests for models/amenity module(Amenity)
"""

import unittest
from models.review import Review
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.c1 = Review()

    def test_inheritance(self):
        """Test if is inheriated from BaseModel"""
        self.assertIsInstance(self.c1, Review)
        self.assertIsInstance(self.c1, BaseModel)

    def test_existing_attributes(self):
        """test if attributes is existing"""
        attr_lst = dir(self.c1)
        self.assertIn('place_id', attr_lst)
        self.assertIn('user_id', attr_lst)
        self.assertIn('text', attr_lst)
        self.assertIn("id", attr_lst)
        self.assertIn("created_at", attr_lst)
        self.assertIn("updated_at", attr_lst)

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        self.assertIsInstance(self.c1.user_id, str)
        self.assertIsInstance(self.c1.place_id, str)
        self.assertIsInstance(self.c1.text, str)
