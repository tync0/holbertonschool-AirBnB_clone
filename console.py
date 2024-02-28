#!/usr/bin/python3
import cmd

"""
This module contains the entry point of the command interpreter.
"""


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

    def do_help(self, args):
        """
        Display help information about a specific command
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
