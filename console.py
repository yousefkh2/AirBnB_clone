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


    def __init__(self):
        super().__init__()
        self.objects = storage.all()

    def __is_valid_input(self, line, no_args=1):
        """Check validation of users command arguments"""
        valid_cls = ['BaseModel', 'User', 'City', 'Amenity', 'Place', 'State',
                     'Review']
        args = line.split() if line else []
        msgs = [
            "** class name missing **",
            "** instance id missing **",
            "** attribute name missing **",
            "** value missing **",
            "** attribute name missing **",
            "** value missing **"
                ]
        i = 0
        while (i < no_args):
            if i >= len(args):
                print(msgs[i])
                return False
            if i == 0:
                if args[0] not in valid_cls:
                    print("** class doesn't exist **")
                    return False
            if i == 1:
                if ".".join(args[:2]) not in self.objects:
                    print("** no instance found **")
                    return False
            i += 1
        return True

    def do_create(self, line):
        """Create new instance"""
        if self.__is_valid_input(line):
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """print string representation of instance"""
        # Not that no handling for args more than required and may cause errors
        if self.__is_valid_input(line, 2):
            key = line.replace(" ", ".")
            print(storage.all().get(key))

    def do_destroy(self, line):
        """Delete required instance object"""
        if self.__is_valid_input(line, 2):
            key = line.replace(" ", ".")
            del self.objects[key]
            storage.save()


    def do_all(self, line):
        """print string representation of all objects
        based on valid given class or not"""
        lst = []
        if self.__is_valid_input(line, 1 if line else 0):
            for k, v in self.objects:
                if line and line not in k:
                    continue
                lst.append()
            print(lst)

    def do_update(self, line):
        """Update object attribute"""
        if self.__is_valid_input(line, 4):
            def handle_args(text):
                lst = []
                arg = ""
                is_quote = False
                for char in text:
                    if char == "'" or char == '"':
                        is_quote = not is_quote
                    if char == " " and not is_quote:
                        lst.append(arg)
                        arg = ""
                    else:
                        arg += char
                lst.append(arg)
                return lst
            args = handle_args(line)
            obj = self.objects.get(".".join(args[:2]))
            if hasattr(obj, args[2]):
                obj_attr = getattr(obj, args[2])
                setattr(obj, args[2], type(obj_attr)(args[3]))
            else:
                setattr(obj, args[2], args[3])
            storage.save()

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
