#!/usr/bin/env python3
"""
defines the FileStorage class
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # path to JSON file
    __file_path = 'file.json'
    # storage for all objects
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self. __objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_objs = {}
        for key in self.__objects:
            json_objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dumps(json_objs, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

    def classes(self):
        """Returns alist of classes"""
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "Amenity": Amenity,
                "City": City,
                "Review": Review
                }
        return classes
