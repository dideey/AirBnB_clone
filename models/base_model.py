#!/usr/bin/python3
import uuid
import datetime
import models

"""
in order to use uuiid
"""
class BaseModel:
    def __init__(self, *_, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if '__class__' in kwargs:
                    continue

                if key in ['created_at', 'updated_at']:
                    value = datetime.datetime.strptime('value', '%Y-%m-%d %H:%M:%S.%f')

                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now().isoformat()
            self.updated_at = datetime.datetime.now().isoformat()
            models.storage.new(self)
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        
        self.updated_at = datetime.datetime.now().isoformat()
        models.storage.save()

    
    
    def to_dict(self):
        """
         returns a dictionary containing all keys/values of __dict__ of the instance
        """
        return {
            **self.__dict__,
            '__class__': self.__class__.__name__,

        }