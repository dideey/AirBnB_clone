#!/usr/bin/python3
"""test module"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """City tests"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(City, BaseModel))
