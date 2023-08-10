#!/usr/bin/python3
"""
Entry point

Run AirBnB web application from console
"""

import cmd

class HBNBCommand(cmd.Cmd):




    def quit(self):
        """Exit the programe"""
        pass

    def do_EOF(self):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
