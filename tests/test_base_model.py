#!/usr/bin/python3
"""Test for base_models.
classes:
    TestBaseModel
"""
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittest for the best model class"""

    def test_init(self):
        """Tests iniitialization new"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

#    def test_init_with_args(self):
#        """Tests initialization with empty args and kwargs."""
#        base_model = BaseModel()
#        self.assertIsInstance(base_model.id, str)
#        self.assertIsInstance(base_model.created_at, datetime)
#        self.assertIsInstance(base_model.updated_at, datetime)
#        self.assertEqual(base_model.created_at, base_model.updated_at)
#
#    def test_init_with_kwargs(self):
#        """Tests initialization with specific id,
#        created_at, and updated_at."""
#        test_id = "test-id"
#        test_created_at = datetime.now(timezone.utc) - timedelta(days=1)
#        test_updated_at = datetime.now(timezone.utc)
#
#        base_model = BaseModel(id=test_id,
#                               created_at=test_created_at.isoformat(),
#                               updated_at=test_updated_at.isoformat())

#        self.assertEqual(base_model.id, test_id)
#        self.assertEqual(base_model.created_at, test_created_at)
#        self.assertEqual(base_model.updated_at, test_updated_at)

#    @patch('base_model.datetime.now')
#    def test_init_with_invalid_datetime_format(self, mock_datetime):
#        """Tests initialization with invalid datetime format in kwargs."""
#        invalid_datetime_str = "invalid_format"
#
#        mock_datetime.return_value = datetime.utcnow()
#
#        with self.assertRaises(ValueError):
#            BaseModel(created_at=invalid_datetime_str)

    def test_str(self):
        """Tests __str__ method representation."""
        this_base_model = BaseModel()
        class_name = this_base_model.__class__.__name__
        instance_id = this_base_model.id
        instance_dict = this_base_model.__dict__
        expected_str = f"[{class_name}] ({instance_id}) {instance_dict}"
        self.assertEqual(str(this_base_model), expected_str)

    def test_save(self):
        """Tests save method updates updated_at."""
        this_base_model = BaseModel()
        initial_updated_at = this_base_model.updated_at

        current_updated_at = this_base_model.save()

        self.assertNotEqual(current_updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests to_dict method returns a dictionary representation."""
        this_base_model = BaseModel()

        base_model_dict = this_base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict["__class__"], 'BaseModel')
        self.assertEqual(base_model_dict['id'], this_base_model.id)
        self.assertEqual(base_model_dict['created_at'],
                         this_base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'],
                         this_base_model.updated_at.isoformat())
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
