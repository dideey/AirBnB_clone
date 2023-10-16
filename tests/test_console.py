#!/usr/bin/python3
"""test module"""
import unittest
from console import HBNBCommand
import cmd


class TestConsole(unittest.TestCase):
    """console test"""
    def test_inheritance(self):
        """check if subclass"""
        self.assertTrue(issubclass(HBNBCommand, cmd.Cmd))
