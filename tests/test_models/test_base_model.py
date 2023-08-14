#!/usr/bin/python3
"""
Tests for base_model module(BaseModel)
"""

import unittest
import datetime as dt
import models
import sys
import json
from models.base_model import BaseModel
import time


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Intitalize objects"""
        self.bs1 = BaseModel()
        self.bs2 = BaseModel()
        self.bs3 = BaseModel()

    def test_attributes_types(self):
        """Assert that object attributes has right types"""
        self.assertIsInstance(self.bs1.id, str)
        self.assertIsInstance(self.bs1.created_at, dt.datetime)
        self.assertIsInstance(self.bs1.updated_at, dt.datetime)

    def test_uniqu_id(self):
        """check if each instance has unique id"""
        self.assertNotEqual(self.bs1.id, self.bs2.id)
        self.assertNotEqual(self.bs2.id, self.bs3.id)

    def test_dict_representation(self):
        """check object dictionary representation"""
        obj_dict = self.bs1.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(self.bs1.id, obj_dict['id'])

    def test_dict_additional_attrs(self):
        """check if dictionary representation has addtitional required keys"""
        obj_dict = self.bs1.to_dict()

        self.assertIn('__class__', obj_dict)
        self.assertEqual('BaseModel', obj_dict['__class__'])

    def test_save(self):
        """Test saving objects"""
        time.sleep(.00001)
        self.bs1.save()
        self.assertNotEqual(self.bs1.created_at.isoformat(),
                              self.bs1.updated_at.isoformat())
        self.assertIn(self.bs1.__class__.__name__ + "." + self.bs1.id,
                      models.storage.all())

    def test_string_representaion(self):
        """Check Correctly formatting string representation"""
        str_rep = "[{}] ({}) {}".format(self.bs1.__class__.__name__, self.bs1.id,
                                        self.bs1.__dict__)
        self.assertEqual(str_rep, self.bs1.__str__())
