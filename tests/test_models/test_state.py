#!/usr/bin/python3
"""test module"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """State tests"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(State, BaseModel))
