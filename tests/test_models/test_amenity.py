#!/usr/bin/python3
"""
Contains the TestAmenity class
"""
import unittest
import inspect
from models.base_model import BaseModel
from models import amenity
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        a = Amenity()
        n_d = amenity.to_dict()
        self.assertEqual(n_d["__class__"], "Amenity")
        self.assertEqual(type(n_d["created_at"]), str)
        self.assertEqual(type(n_d["updated_at"]), str)
        self.assertEqual(n_d["created_at"], a.created_at.strftime(time_format))
        self.assertEqual(n_d["updated_at"], a.updated_at.strftime(time_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_uuid(self):
        """test that id is str"""
        inst_n = Amenity()
        self.assertIs(type(inst_n.id), str)


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
