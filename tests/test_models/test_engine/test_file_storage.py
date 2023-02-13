#!/usr/bin/python3
"""
test_file_storage module - Contains the TestFileStorage classes
"""
import unittest
from models import storage


class TestFileStorage(unittest.TestCase):
    """ class for testing State class"""
    def test_dict(self):
        """test if all return dictionary"""
        obj = storage.all()
        self.assertEqual(type(obj), dict)
