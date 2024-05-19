#!/usr/bin/python3

import uuid
from datetime import datetime

"""
Module containing class BaseModel
that defines all common attributes/methods for other classes
"""

class BaseModel:
     """Defines all common attributes/methods for other classes."""

     def __init__(self):
         """To initialize an instance of BaseModel."""
         self.id = str(uuid.uuid4())
         self.created_at = datetime.now()
         self.updated_at = self.created_at

     def __str__(self):
         """Always returns string representation of called instance."""
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

     def save(self):
         """Updates `updated_at` with the current date and time."""
         self.updated_at = datetime.now()

     def to_dict(self):
         """Returns a dictionary containing all keys/values of __dict__"""
         dict_container = self.__dict__.copy()
         dict_container['__class__'] = self.__class__.__name__
         dict_container['created_at'] = self.created_at.isoformat()
         dict_container['updated_at'] = self.updated_at.isoformat()
         return dict_container
