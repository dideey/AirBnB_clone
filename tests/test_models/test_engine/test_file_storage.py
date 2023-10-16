#!/usr/bin/python3
"""test module"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """FileStorage tests"""
    def test_Storage(self):
        """
        check objects
        """
        storage = FileStorage()
        objects = storage.all()
        for value in objects.values():
            self.assertFalse(value == dict)