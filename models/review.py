#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = "Place.id"
    user_id = "User.id"
    text = ""
