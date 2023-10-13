#!/usr/bin/python3
import uuid
import datetime
import models

"""
in order to use uuiid
"""
class BaseModel:
    def __init__(self, *_, **kwargs):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    self.__class__.__name__ = value
                elif key == 'created_at':
                    self.created_at = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    
    
    def to_dict(self):
        """
         returns a dictionary containing all keys/values of __dict__ of the instance
        """
        # return {
        #     **self.__dict__,
        #     '__class__': self.__class__.__name__,

        # }
        dict_array = {}
        for key, value in self.__dict__.items():
            if key != 'created_at' and key != 'updated_at':
                dict_array[key] = value
        dict_array['__class__'] = self.__class__.__name__
        dict_array['created_at'] = self.created_at.isoformat()
        dict_array['updated_at'] = self.updated_at.isoformat()
        return dict_array