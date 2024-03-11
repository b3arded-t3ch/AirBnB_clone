#!/usr/bin/python3
'''
This script contains a class BaseModel
that defines all common attributes/methods for other classes
'''
import uuid
import datetime
import models


class BaseModel:
    """
    This is the base class from which other
    classes inherit.
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def __str__(self):
        """
        prints a string representation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        returns a dictionary of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = __class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __init__(self, *args, **kwargs):
        """
        initiates a new instance with the attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
