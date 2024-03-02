#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command-line interface for the AirBnB clone.
    It provides various commands for interacting with the application.
    """

    prompt = "(hbnb) "
    All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, args):
        """
        Quit the command-line interface.
        """
        return True

    def do_EOF(self, args):
        """
        Handle the end-of-file signal.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, args):
        """
        Create an instance of BaseModel
        """
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

    def do_show(self, args):
        """
        Show an instance of BaseModel based on id
        """

        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            print(str(obj[obj_key]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete an instance of BaseModel based on id
        """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            del obj[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Show all instances
        """
        storage.reload()
        json_dict = []
        obj_dict = storage.all()
        if line == "":
            for key, value in obj_dict.items():
                json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        arg = shlex.split(line)
        if arg[0] in HBNBCommand.All_class_dict.keys():
            for key, value in obj_dict.items():
                if arg[0] in key:
                    json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update given instance based on id
        """
        if not line:
            print("** class name missing **")
            return
        arg = shlex.split(line)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(arg) == 2):
            print("** attribute name missing **")
            return
        if (len(arg) == 3):
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if arg[2] in obj_dict.keys():
            d_type = type(obj_dict[arg[2]])
            print(d_type)
            obj_dict[arg[2]] = type(obj_dict[arg[2]])(arg[3])
        else:
            obj_dict[arg[2]] = arg[3]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
