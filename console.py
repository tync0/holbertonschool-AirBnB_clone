#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command-line interface for the AirBnB clone.
    It provides various commands for interacting with the application.
    """

    prompt = "(hbnb) "
    classes = [
        "BaseModel",
    ]

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

    def do_create(self, line):
        """
        Create an instance of BaseModel
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()

    def do_show(self, line):
        """
        Show an instance of BaseModel based on id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """
        Delete an instance of BaseModel based on id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
        Show all instances
        """
        args = line.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            key = args[1]
            print(
                [
                    str(value)
                    for value in storage.all().values()
                    if value.__class__.__name__ == key
                ],
            )

    def do_update(self, line):
        """
        Update given instance based on id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
                att_name = args[2]
                value = args[3]
                if type(value) is int:
                    setattr(instance, att_name, int(value))
                elif type(value) is float:
                    setattr(instance, att_name, float(value))
                else:
                    value = value[1:-1]
                    setattr(instance, att_name, str(value))
                instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
