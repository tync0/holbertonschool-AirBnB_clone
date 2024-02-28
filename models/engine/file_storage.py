#!/usr/bin/python3
import json
import os.path as path
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
            for key in data:
                FileStorage.__objects[key] = BaseModel(**data[key])

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()
