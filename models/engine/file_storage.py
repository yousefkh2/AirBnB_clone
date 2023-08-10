#!/usr/bin/python3
"""
Module: engine

mange saved and loaded files
"""
import json

class FileStorage:
    """
    storage objects to file and retrieve them
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Get all current objects"""
        return self.__objects

    def new(self, obj):
        """Add new object to current objects"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Save json string to file"""
        objects_dict = {}
        for k, v in self.__objects.items():
            objects_dict[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(objects_dict))

    def reload(self):
        """Load objects file and deserialize them to objects"""
        try:
            with open(self.__file_path, "r") as f:
                objects_dict = json.loads(f.read())
                for k, v in objects_dict.items():
                    obj = eval(v['__class__'])(v)
                    self.new(obj)
        except FileNotFoundError:
            pass
