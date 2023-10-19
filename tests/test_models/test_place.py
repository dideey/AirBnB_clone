#!/usr/bin/python3
"""test module"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Place tests"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(Place, BaseModel))
