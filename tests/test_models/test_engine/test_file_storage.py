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


    def test_file_existance(self):
        pass

    def test_storage_types(self):
        pass
