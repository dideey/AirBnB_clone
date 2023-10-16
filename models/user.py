#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *_, **kwargs):
        super().__init__(*_, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
