#!/usr/bin/python3
"""
Entry point

Run AirBnB web application from console
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """TT"""
    prompt = '(hbnb)'

    def __is_valid_input(self, line):
        valid_cls = ['BaseModel', 'User']
        msgs = ["** class name missing **",
                "** class doesn't exist **",
                "** instance id missing **"
                ]
        args = line.split()
        is_valid = True
        for _ in range(no_args):
            if args[] : #Not complete
                print("")
        return is_valid

    def do_create(self, obj_cls):
        """Create new instance from valid class"""
        if self.__is_valid_input(obj_cls):
            obj = eval(obj_cls)()
            obj.save()
            print(obj.id)


    def do_show(self, line):
        """print string representation of instance"""
        #Not that no handling for args more than required
        if self.__is_valid_input(line, 'show'):
            key = line.replace(" ", ".")
            print(storage.all().get(key, "** no instance found **")) 

    def do_destroy(self, line):
        """Delete required instance object"""
        if self.__is_valid_input(line, 'destroy'):
            key = line.replace(" ", ".")
            objects = storage.all()
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")

    def do_all(self, line):
        """print string representation of all objects
        based on given class or not"""
        if self.__is_valid_input(line):
            lst = []
            objects = storage.all()
            

    def emptyline(self):
        pass

    def do_quit(self, line):
        """command to exit the programe"""
        return True

    def help_quit(self):
        print("Quit Command to exit the program\n")

    def do_EOF(self, line):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
