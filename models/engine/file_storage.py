#!/usr/bin/python3
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


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

    def classes(self):
        """
        Returns alist of classes
        """
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "Amenity": Amenity,
                "City": City,
                "Review": Review
                }
        return classes
