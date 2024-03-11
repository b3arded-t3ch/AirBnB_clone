from models.base_model import BaseModel


class City(BaseModel):
    '''
    a class City that inherits from BaseModel
    '''
    state_id = ""
    name = ''

    def __str__(self):
        '''print the documentation of the class'''
        new_dict = self.__dict__.copy()
        return f"[{__class__.__name__}] ({self.id}) {new_dict}"

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of the instance
        '''
        dict_copy = self.__dict__.copy()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['__class__'] = __class__.__name__
        dict_copy['id'] = self.id
        return dict_copy
