#!/usr/bin/python3
"""
base_model module
"""

import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Super class from which other instances will be derived from"""
    def __init__(self, *args, **kwargs):
        """instance method for initializing new objects"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of an object"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                            self.id, self.__dict__)

    def save(self):
        """update the public instance attribute updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """dictionary representation of object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__self__
        if 'created_at' in obj_dict:
            #obj_dict['created_at'] = datetime.isoformat(obj_dict['created_at'])
            obj_dict['created_at'] = obj_dict['created_at'].strftime(time)
        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = obj_dict['updated_at'].strftime(time)
        return obj_dict
