#!/usr/bin/python3
"""
Tests for models/user module(User)
"""

import unittest
from models.user import User
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.c1 = User()

    def test_inheritance(self):
        """Test if is inheriated from BaseModel"""
        self.assertIsInstance(self.c1, User)
        self.assertIsInstance(self.c1, BaseModel)

    def test_existing_attributes(self):
        """test if attributes is existing"""
        attr_lst = dir(self.c1)
        self.assertIn('first_name', attr_lst)
        self.assertIn('last_name', attr_lst)
        self.assertIn('password', attr_lst)
        self.assertIn('email', attr_lst)
        self.assertIn("id", attr_lst)
        self.assertIn("created_at", attr_lst)
        self.assertIn("updated_at", attr_lst)

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        self.assertIsInstance(self.c1.email, str)
        self.assertIsInstance(self.c1.password, str)
