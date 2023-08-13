#!/usr/bin/python3
"""
Tests for models/state module(State)
"""

import unittest
from models.state import State
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel

class TestState(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.c1 = State()

    def test_inheritance(self):
        """Test if is inheriated from BaseModel"""
        self.assertIsInstance(self.c1, State)
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
