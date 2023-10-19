#!/usr/bin/python3
"""test module"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """User tests"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(User, BaseModel))
