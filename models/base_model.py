#!/usr/bin/env python3
"""
base_model module
"""
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """instance method for initializing new objects"""
        if kwargs:
            self.__dict__ = kwargs['__dict__']
            created = datetime.fromisoformat(kwargs['created_at'])
            updated = datetime.fromisoformat(kwargs['updated_at'])
            self.created_at = created
            self.updated_at = updated
        else:
            id = str(uuid.uuid4())
            created_at = datetime.now()
            updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of an object"""
        return ("[{0:s}] ({1:s}) {2}".
                format(self.__class__, self.id, self.__dict__))

    def save(self):
        """update the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary representation of object"""
        dictionary = {}
        dictionary["__class__"] = self.__class__
        dictionary["created_at"] = datetime.isoformat(self.created_at)
        dictionary["updated_at"] = datetime.isoformat(self.updated_at)
        return dictionary
