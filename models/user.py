#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    def __init__(self):
        """initiation"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
