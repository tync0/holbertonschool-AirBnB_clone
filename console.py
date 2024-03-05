#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command-line interface for the AirBnB clone.
    It provides various commands for interacting with the application.
    """

    prompt = "(hbnb) "

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
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] == "BaseModel":
            new_inst = BaseModel()
            new_inst.save()

    def do_show(self, args):
        """
        Show an instance of BaseModel
        """
        print(args[0] == "BaseModel")
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
