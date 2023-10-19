#!/usr/bin/python3
"""test module"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Amenity tests"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(Amenity, BaseModel))
