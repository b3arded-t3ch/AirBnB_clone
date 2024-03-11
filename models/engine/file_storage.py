#!/usr/bin/python3
"""
Manages the serialisation and deserialisation of BaseModel objects
"""
import json
from models.base_model import BaseModel 
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review 
from models.user import User
import os

class FileStorage:
    """The base class for encoding and decoding process"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary representation of all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name_of_class = obj.__class__.__name__
        key = f"{name_of_class}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        __objects_dict = {
                key: value.to_dict()
                for key, value in self.__objects.items()
                }
        try:
            with open(self.__file_path, 'w') as file:
                json.dump(__objects_dict, file)
            return True
        except (OSError, TypeError) as e:
            return False

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as json_file:
                try:
                    data_dict = json.load(json_file)
                    for k, v in data_dict.items():
                        class_name, obj_id = k.split('.')
                        cls = eval(class_name)
                        intnc = cls(**v)
                        self.__object[k] = instnc
                except Exception:
                    pass
