#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def save(self):
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
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

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
