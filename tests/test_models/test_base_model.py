#!/usr/bin/python3
"""
Tests for base_model module(BaseModel)
"""

import unittest
from models.base_model import BaseModel
import datetime as dt

class TestBaseModel(unittest.Testcase):

    def setUp(self):
        """Intitalize objects"""
        bs1 = BaseModel()
        bs2 = BaseModel()
        bs3 = BaseModel()

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        self.assertIsInstance(bs1.id, str)
        self.assertIsInstance(bs1.created_at, dt.datetime)
        self.assertIsInstance(bs1.updated_at, dt.datetime)

    def test_uniqu_id(self):
        """check if each instance has unique id"""
        self.assertNotEqual(bs1.id, bs2.id)
        self.assertNotEqual(bs2.id, bs3.id)

    def test_dict_representation(self):
        """check object dictionary representation"""
        obj_dict = bs1.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(bs1.id, obj_dict['id'])

    def test_dict_additional_attrs(self):
        """check if dictionary representation has addtitional required keys"""
        obj_dict = bs1.to_dict()

        self.assertIn('__class__', obj_dict)
        self.assertEqual('BaseModel', obj_dict['__class__'])
