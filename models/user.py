#!/usr/bin/python3
from models.base_model import BaseModel
class User(BaseModel):
    def __init__(self):
        self.email = ""
        self.password = ""
        self.First_name = ""
        self.Last_name = ""
        