#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as jfile:
            json.dump(json_dict, jfile)
    
    def reload(self):
        try:
             with open(self.__file_path, mode="r", encoding="UTF8") as file:
                jdata = json.load(file)
        except Exception:
            pass