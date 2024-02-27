#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, key, value)
                else:
                    setattr(self, key, datetime.datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__,
        )

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
