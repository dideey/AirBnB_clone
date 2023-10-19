#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
