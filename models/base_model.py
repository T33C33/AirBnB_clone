#!/usr/bin/python3
"""Module containing class BaseModel that"""
import uuid
from datetime import datetime, timezone

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid())
        
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        
    def save(self):
        """
        Updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now(timezone.utc)
        
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        
        return inst_dict
    
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)