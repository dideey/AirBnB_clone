#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    def __init__(self):
        """initiation"""
        self.state_id = "State.id"
        self.name = ""
