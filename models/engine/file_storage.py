#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def save(self):
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
            for key in data:
                FileStorage.__objects[key] = BaseModel(**data[key])
        except Exception:
            pass

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()
