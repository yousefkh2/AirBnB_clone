#!/usr/bin/python3
"""
Module_name: model

Create base object, it will be useful to be used as superclass
"""

import datetime as dt
import uuid

class BaseModel:
    """
    Base class to be inherited

    Attr:
       id: uniq identifier for all instances
       created_at: datetime(ISO format) of instance created time
       updated_at: datetime(ISO format) of any object change
    """

    def __init__(self, *arg, **kwarg):
        if kwarg:
            self.__from_dict(kwarg)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()

    def __from_dict(self, kwarg):
        """create an instace from given dictionary"""
        for attr, value in kwarg.items():
            if attr != "__class__":
                setattr(self, attr, value)
        self.created_at = dt.datetime.strptime(self.created_at,
                                               "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = dt.datetime.strptime(self.updated_at,
                                               "%Y-%m-%dT%H:%M:%S.%f")
    
    def save(self):
        """update attributes"""
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        """Create a dictionary from object attributes"""
        ins_dict = self.__dict__
        ins_dict["__class__"] = self.__class__.__name__
        ins_dict["created_at"] = ins_dict["created_at"].isoformat()
        ins_dict["updated_at"] = ins_dict["updated_at"].isoformat()
        return ins_dict

    def __str__(self):
        """Instance string repr"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))
    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))
    print("--")
    print(my_model is my_new_model)
