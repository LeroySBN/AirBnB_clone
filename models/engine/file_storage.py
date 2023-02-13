#!/usr/bin/env python3
"""
defines the FileStorage class
"""
import json

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
            # for each line deserialize and add to __objects dict
            with open(self.__file_path, 'r') as f:
                j_obj = json.load(f)
            for key in instances:
                self.__objects[key] = classes[j_obj
                                              [key]['__class__']]{**j_obj[key])
        except FileNotFoundError:
            pass
