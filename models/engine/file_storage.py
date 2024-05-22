#!/usr/bin/python3
""" JSON file storage """


import json

class FileStorage:
    """ class serializes instances to a JSON file and deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return (self.__objects)
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        pass

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        pass

    def reload(self):
        """ deserializes the JSON file to objects """
        pass
