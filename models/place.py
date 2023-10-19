#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    def __init__ (self):
        self.city_id = "City.id"
        self.user_id = "User.id"
        self.name = ""
        self.description = ""
        self.number_rooms = int
        self.number_bathrooms = int
        self.max_guest = int
        self.price_by_night = int
        self.latitude = float
        self.longitude = float
        self.amenity_ids = []
        