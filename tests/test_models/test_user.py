#!/usr/bin/python3
"""
Tests for models/user module(User)
"""

import unittest
from models import user
from models.user import User
from models.base_model import BaseModel
import inspect


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    # def test_pep8_conformance_user(self):
    #     """Test that models/user.py conforms to PEP8."""
    #     pep8s = pep8.StyleGuide(quiet=True)
    #     result = pep8s.check_files(['models/user.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    # def test_user_func_docstrings(self):
    #     """Test for the presence of docstrings in User methods"""
    #     for func in self.user_f:
    #         self.assertIsNot(func[1].__doc__, None,
    #                          "{:s} method needs a docstring".format(func[0]))
    #         self.assertTrue(len(func[1].__doc__) >= 1,
    #                         "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Initialize objects"""
        self.c1 = User()

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.c1, User)
        self.assertIsInstance(self.c1, BaseModel)

    def test_existing_attributes(self):
        """test if attributes exist"""
        attr_lst = dir(self.c1)
        self.assertIn('first_name', attr_lst)
        self.assertIn('last_name', attr_lst)
        self.assertIn('password', attr_lst)
        self.assertIn('email', attr_lst)
        self.assertIn("id", attr_lst)
        self.assertIn("created_at", attr_lst)
        self.assertIn("updated_at", attr_lst)

    def test_attributes_types(self):
        """Assert that object attributes have the right types"""
        self.assertIsInstance(self.c1.email, str)
        self.assertIsInstance(self.c1.password, str)
        self.assertIsInstance(self.c1.first_name, str)
        self.assertIsInstance(self.c1.last_name, str)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        new_d = self.c1.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in self.c1.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_d = self.c1.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], self.c1.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], self.c1.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        string = "[User] ({}) {}".format(self.c1.id, self.c1.__dict__)
        self.assertEqual(string, str(self.c1))
