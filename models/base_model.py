#!/usr/bin/env python3
"""
base_model module
"""

import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    def __init__(self, *args, **kwargs):
        """instance method for initializing new objects"""
        if kwargs:
            self.__dict__ = kwargs['__dict__']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns string representation of an object"""
        return "[{0:s}] ({1:s}) {2}".
                format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """dictionary representation of object"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        if 'created_at' in obj_dict:
            obj_dict['created_at'] = datetime.isoformat(obj_dict['created_at'])
            # obj_dict['created_at'] = obj_dict['created_at'].strftime(time)
        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = obj_dict['updated_at'].strftime(time)
        return obj_dict
