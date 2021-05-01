#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            try:
                new_obj = {}
                for el_key, el_val in self.__objects.items():
                    el_name = el_key.split('.')[0]
                    if el_name == cls.__name__:
                        new_obj[el_key] = el_val
                return new_obj
            except Exception:
                raise Exception
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=2)

    def delete(self, obj=None):
        """ delete instance from __object """
        try:
            class_name = obj.__class__.__name__
            obj_ref = class_name + '.' + obj.id
            del (self.__objects[obj_ref])  # try to delete obj from dict
            self.save()  # write into the .json file
        except Exception:
            pass

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
        
       