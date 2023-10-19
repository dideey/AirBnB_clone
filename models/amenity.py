#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self):
        self.name = ""
