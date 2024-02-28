#!/usr/bin/python3
import cmd

"""
This module contains the entry point of the command interpreter.
"""


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return True

    def do_quit(self, agrs):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
