#!/usr/bin/python3
"""
Tests for models/engine/file_storage class(FileStorage)
"""

import unittest
from models.engine.file_storage import FileStorage
import datetime as dt
import models
import sys
import json


class TestFileStorage(unittest.TestCase):
    """Test for storage class"""

    def setUp(self):
        """Intialize file storage instance"""
        self.st = FileStorage()
        self.bs1 = models.base_model.BaseModel()
        self.ur1 = models.user.User()
        self.file_attr = "_FileStorage__file_path"
        self.obj_attr = "_FileStorage__objects"
        self.objects_dict = getattr(self.st, self.obj_attr)
        self.file_obj = getattr(self.st, self.file_attr)

    def test_attributes_types(self):
        """Test types of attributes"""
        self.assertIsInstance(self.objects_dict, dict)
        self.assertIsInstance(self.file_obj, str)

    def test_new(self):
        """Test adding properly new objects to current saved objects"""
        self.st.new(self.bs1)
        self.st.new(self.ur1)
        self.assertIn(self.bs1.__class__.__name__ + "." + self.bs1.id,
                        self.objects_dict)
        self.assertIn(self.ur1.__class__.__name__ + "." + self.ur1.id,
                        self.objects_dict)

    def test_all(self):
        """Test all method"""
        d = self.st.all()
        self.assertIs(d, getattr(FileStorage, self.obj_attr))

    def test_file_existance(self):
        pass

    def test_storage_types(self):
        pass

    def tearDown(self):
        """Remove testing files"""
        
