#!/usr/bin/python3
""" JSON file storage """


import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ class serializes instances to a
    JSON file and deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def all(self):
        """ returns the dictionary __objects """
        return (FileStorage.__objects)

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes the JSON file to objects """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        inst = cls(**value)
                        FileStorage.__objects[key] = inst
                except Exception:
                    pass
