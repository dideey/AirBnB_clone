#!/usr/bin/python3
"""test module"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Review tests"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(Review, BaseModel))
