#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    def __init__(self):
        """initiation"""
        self.place_id = "Place.id"
        self.user_id = "User.id"
        self.text = ""
