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
            json.dump(f, FileStorage.__objects)

    def reload(self):
        file = FileStorage.__file_path
        if path.exists(file):
            with open(file, "r") as f:
                FileStorage.__objects = json.dump(f)

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.name, obj.id)
        FileStorage.__objects[key] = obj.to_dict()
