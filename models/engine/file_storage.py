#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage class"""
    def __init__(self):
        """initiation"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """all function"""
        return self.__objects

    def new(self, obj):
        """new function"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save function"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as jfile:
            json.dump(json_dict, jfile)

    def reload(self):
        """reload function"""
        try:
            with open(self.__file_path, mode="r", encoding="UTF8") as file:
                jdata = json.load(file)
                for value in jdata.values():
                    myModel = value["__class__"]
                    myModel = eval(myModel)
                    obj = myModel(**value)
                    self.new(obj)
        except Exception:
            pass
