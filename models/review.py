 #!/usr/bin/python3
from models.base_model import BaseModel
class Review(BaseModel):
    def __init__(self):
        self.place_id = "Place.id"
        self.user_id = "User.id"
        self.text = ""
        
