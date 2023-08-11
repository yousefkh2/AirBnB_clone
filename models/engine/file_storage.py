#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
     """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key as <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = {}
                loaded_objects = json.load(f)
                for key, value in loaded_objects.items():
                    class_name = value.pop('__class__')
                    cls = globals()[class_name]
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
