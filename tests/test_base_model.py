import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from .models import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_with_args(self):
        """Tests initialization with empty args and kwargs."""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_init_with_kwargs(self):
        """Tests initialization with specific id, created_at, and updated_at."""
        test_id = "test-id"
        test_created_at = datetime.utcnow() - timedelta(days=1)
        test_updated_at = datetime.utcnow()

        base_model = BaseModel(id=test_id, created_at=test_created_at.isoformat(), updated_at=test_updated_at.isoformat())

        self.assertEqual(base_model.id, test_id)
        self.assertEqual(base_model.created_at, test_created_at)
        self.assertEqual(base_model.updated_at, test_updated_at)

    @patch('base_model.datetime.now')
    def test_init_with_invalid_datetime_format(self, mock_datetime):
        """Tests initialization with invalid datetime format in kwargs."""
        invalid_datetime_str = "invalid_format"

        mock_datetime.return_value = datetime.utcnow()

        with self.assertRaises(ValueError):
            BaseModel(created_at=invalid_datetime_str)

    def test_str(self):
        """Tests __str__ method representation."""
        base_model = BaseModel()
        expected_str = f"[{base_model.__class__.__name__}] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        """Tests save method updates updated_at."""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at

        base_model.save()

        self.assertGreater(base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Tests to_dict method returns a dictionary representation."""
        base_model = BaseModel()

        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict["__class__"], base_model.__class__.__name__)
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
