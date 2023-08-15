## AirBnB clone project:
-----------------------------------------------------------------------------
The goal of the project is to deploy on your server a simple copy of the [AirBnB website](https://www.airbnb.com/).we won’t implement all the features, only some of them to cover all fundamental concepts.

we will have a complete web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### How to run from Console?
---------------------------------------------------------------------------------
Run the program useing `./console.py` from project directory.
To see all availabe commands you can type `help`, for example:

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
also, you can get help for specific command by typing command as argument
to help `help create'
only one of the following objects availabe for out project:
BaseModel, User, Place, City, State, Amenity, Review

#### How to use?
- **Create**: create new isntance giving one of valid objects, this command create new
instance and save it. it will print id of new created instance, for example:

```
(hbnb) create BaseModel
00050593-ff38-4186-9907-12bc2094bcae
(hbnb)
```

- **destroy**: Delete saved instance. It takes two arguments object type and id, this command
will delete saved object, for example:

```
(hbnb) destroy BaseModel 00050593-ff38-4186-9907-12bc2094bcae
(hbnb)
```

- **show**: show saved instance attributes. It takes two arguments object type and id, this command will print dictionary of instance attriubtes, for example:

```
(hbnb) show User 16df53d0-0fe1-4c15-8f39-aa516cfb7968
[User] (16df53d0-0fe1-4c15-8f39-aa516cfb7968) {'id': '16df53d0-0fe1-4c15-8f39-aa516cfb7968', 'created_at': datetime.datetime(2023, 8, 13, 14, 50, 37, 110037), 'updated_at': datetime.datetime(2023, 8, 13, 14, 50, 37, 110037)}
(hbnb)
```

- **all**: print a list of all saved instance. also, you can pass given object type as argument
to this command, in this case it will only display all availabe objects for given type. 
for example:

```
(hbnb) all
["[BaseModel] (00050593-ff38-4186-9907-12bc2094bcae) {'id': '00050593-ff38-4186-9907-12bc2094bcae', 'created_at': datetime.datetime(2023, 8, 13, 14, 41, 28, 369536), 'updated_at': datetime.datetime(2023, 8, 13, 14, 41, 28, 369536)}", "[User] (16df53d0-0fe1-4c15-8f39-aa516cfb7968) {'id': '16df53d0-0fe1-4c15-8f39-aa516cfb7968', 'created_at': datetime.datetime(2023, 8, 13, 14, 50, 37, 110037), 'updated_at': datetime.datetime(2023, 8, 13, 14, 50, 37, 110037)}"]
(hbnb) all BaseModel
["[BaseModel] (00050593-ff38-4186-9907-12bc2094bcae) {'id': '00050593-ff38-4186-9907-12bc2094bcae', 'created_at': datetime.datetime(2023, 8, 13, 14, 41, 28, 369536), 'updated_at': datetime.datetime(2023, 8, 13, 14, 41, 28, 369536)}"]
(hbnb) all User
["[User] (16df53d0-0fe1-4c15-8f39-aa516cfb7968) {'id': '16df53d0-0fe1-4c15-8f39-aa516cfb7968', 'created_at': datetime.datetime(2023, 8, 13, 14, 50, 37, 110037), 'updated_at': datetime.datetime(2023, 8, 13, 14, 50, 37, 110037)}"]
(hbnb) all City
[]
(hbnb)
```

- **update**: update existing object attributes, pass the following arguments to this command
__(object_type, object_id, attribute_name, attribute_value)__, you should pass string
argument inside double quota. see restriction for more details. for example:

```
(hbnb) update User 16df53d0-0fe1-4c15-8f39-aa516cfb7968 name "anas"
(hbnb)
```

- **quit**: exit the program

#### Restricions:
- This program handls only the following:
  - object type
  - not existing object
  - missing arguments
- You can assume arguments are always in the right order
- Each arguments are separated by a space
- A string argument with a space must be between double quote
- The error management starts from the first argument to the last one
