#!/usr/bin/python3
"""
Entry point

Run AirBnB web application from console
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Intialize User console commands"""
    prompt = '(hbnb) '

    def __is_valid_input(self, line, no_args=1, objects={}):
        """Check validation of users command arguments"""
        valid_cls = ['BaseModel', 'User', 'City', 'Amenity', 'Place', 'State',
                     'Review']
        args = line.split() if line else []
        msgs = [
            "** class name missing **",
            "** instance id missing **",
            "** attribute name missing **",
            "** value missing **"
                ]
        i = 0
        while (i < no_args):
            if i >= len(args):
                print(msg[i])
                return False
            if i == 0:
                if args[0] is not in valid_cls:
                    print("** class doesn't exist **")
                    return False
            if i == 1:
                if ".".join(args[:2]) is not in objects:
                    print("** no instance found **")
            i += 1
        # if line:
        #     args = line.split()
        #     if args[0] not in valid_cls:
        #         print(msgs[1])
        #         return False
        #     elif len(args) < no_args:
        #         print(msgs[2])
        #         return False
        # else:
        #     print(msgs[0])
        #     return False
        # return True

    def do_create(self, line):
        """Create new instance"""
        if self.__is_valid_input(line):
            obj = eval(line)()
            obj.save()
            print(obj.id)


    def do_show(self, line):
        """print string representation of instance"""
        # Not that no handling for args more than required and may cause errors
        objects = storage.all()
        if self.__is_valid_input(line, 2, objects):
            key = line.replace(" ", ".")
            print(storage.all().get(key))

    def do_destroy(self, line):
        """Delete required instance object"""
        objects = storage.all()
        if self.__is_valid_input(line, 2, objects):
            key = line.replace(" ", ".")
            del objects[key]
            storage.save()


    def do_all(self, line):
        """print string representation of all objects
        based on valid given class or not"""
        objects = storage.all()
        if not line:
            for v in objects.values():
                print(v)
        elif self.__is_valid_input(line, 1):
            for k, v in objects.items():
                if line in k:
                    print(v)

    def do_update(self, line):
        if self.__is_valid_input(line, 4):
            args = line.split()[:4]
            

    def emptyline(self):
        """handling emptyline command"""
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
