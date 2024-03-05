#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """ Serializes instances to JSON file
    and deserializes JSON file to instances """

    __file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "file.json"))
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        my_dict = {}

        for keys, val in self.__objects.items():
            ''' serialize each object using the key '''
            my_dict[keys] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            my_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
            if not os.path.isfile(self.__file_path):
                return
            with open(self.__file_path, "r") as file_path:
                objects = json.load(file_path)
                self.__objects = {}
                for key in objects:
                    name = key.split(".")[0]
                    self.__objects[key] = my_dict[name](**objects[key])
        except FileNotFoundError:
            pass
