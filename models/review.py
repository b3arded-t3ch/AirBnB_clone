#!/usr/bin/python3
'''
review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    a class Place that inherits from BaseModel
    '''
    place_id = ""
    user_id = ""
    text = ''

    def __str__(self):
        '''print the documentation of the class'''
        new_dict = self.__dict__.copy()
        return f"[{__class__.__name__}] ({self.id}) {new_dict}"

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of the instances
        '''
        dict_copy = self.__dict__.copy()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['__class__'] = __class__.__name__
        dict_copy['id'] = self.id
        return dict_copy
