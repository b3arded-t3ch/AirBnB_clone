#!/usr/bin/python3
import cmd, sys
from models.base_model import BaseModel
from models.user import User  
from models.review import Review 
from models.state import State  
from models.city import City
from models.place import Place
from models.amenity import Amenity  
from models import storage

class HBNBCommand(cmd.Cmd):
    '''HBNB command processor'''
    prompt = "(hbnb) "

    def do_EOF(self, line):
        '''end of file'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        print

    def do_create(self, class_name):
        '''
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        '''
        if not class_name:
            print("** class name missing **")
        elif class_name != "BaseModel" and class_name != "User" and\
        class_name != "Place" and class_name != "State" and class_name != "City" and\
        class_name != "Review" and class_name != "Amenity":
            print("** class doesn't exist **")
        else:
            if class_name == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            elif class_name == "User":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif class_name == "Place":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif class_name == "State":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif class_name == "City":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif class_name == "Amenity":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif class_name == "Review":
                new_instance = User()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, class_detail):
        '''
        Prints the string representation of an 
        instance based on the class name and
        '''
        if not class_detail:
            print("** class name missing **")
            return
        split_update = class_detail.split()
        class_name = split_update[0]
        if class_name != "BaseModel" and class_name != "User" and\
        class_name != "Place" and class_name != "State" and class_name != "City" and\
        class_name != "Review" and class_name != "Amenity":
            print("** class doesn't exist **")
            return
        if len(split_update) != 2:
            print("** instance id missing **")
            return
        class_id = split_update[1]
        all_objects = storage.all()
        for obj_id in all_objects.keys():
            obj = all_objects[obj_id]
            if obj.id == class_id:
                print(f"{obj}")
                return
        print("** no instance found **")

    def do_destroy(self, destroy_data):
        '''
        Deletes an instance based on the class 
        name and id (save the change into the JSON file)
        '''
        if not destroy_data:
            print("** class name missing **")
            return
        split_update = destroy_data.split()
        class_name = split_update[0]
        if class_name != "BaseModel" and class_name != "User" and\
        class_name != "Place" and class_name != "State" and class_name != "City" and\
        class_name != "Amenity" and class_name != "Review":
            print("** class doesn't exist **")
            return
        if len(split_update) != 2:
            print("** instance id missing **")
            return
        class_id = split_update[1]
        all_objects = storage.all()
        for obj_id in all_objects.keys():
            obj = all_objects[obj_id]
            if obj.id == class_id:
                del obj.id
                for key, value in obj.__dict__.items():
                    del value
                return
        print("** no instance found **")

    def do_all(self, class_name):
        '''
        Prints all string representation of all
        instances based or not on the class name.
        '''
        if not class_name:
            print("** class name missing **")
            return
        if class_name != "BaseModel" and class_name != "User" and\
        class_name != "Place" and class_name != "State" and\
        class_name != "City" and class_name != "Amenity" and class_name != "Review":
            print("** class doesn't exist **")
            return

        print([str(storage.all()[obj_id]) for obj_id in storage.all().keys()])
        '''
        all_objects = storage.all()
        data_list = []
        for obj_id in all_objects.keys():
            obj = str(all_objects[obj_id])
            data_list.append(obj)
        print(data_list)
        '''

    def do_update(self, update_data):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        '''
        if not update_data:
            print("** class name missing **")
            return
        split_update = update_data.split()
        class_name = split_update[0]
        if class_name != "BaseModel" and class_name != "User" and\
        class_name != "Place" and class_name != "State" and class_name != "City" and\
        class_name != "Amenity" and class_name != "Review": 
            print("** class doesn't exist **")
            return
        if not len(split_update) > 2:
            print("** instance id missing **")
            return
        class_id = split_update[1]
        all_objects = storage.all()
        for obj_id in all_objects.keys():
            obj = all_objects[obj_id]
            if obj.id != class_id:
                print("** no instance found **")
                return
            else:
                attribute_name = split_update[2]
                for key in obj.__dict__.keys():
                    if attribute_name == key:
                        if len(split_update) != 4:
                            print("** value missing **")
                            return
                        else:
                            attribute_value = split_update[3]
                            obj.__dict__[key] = attribute_value
                            obj.save()
                            return

                print("** attribute name missing **")
                return
    
    def do_User(self, class_data):
        '''
        retrieve all instances of a class
        '''
        all_objects = storage.all()
        class_list = []
        for obj_class in all_objects.keys():
            obj = all_objects[obj_class]
            if obj.__class__.__name__ == "User":
                class_list.append(str(obj))
        print(class_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
