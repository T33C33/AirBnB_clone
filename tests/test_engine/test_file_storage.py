#!/usr/bin/python3
import models
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_file_storage(unittest.TestCase):
    """Test for file_storage.py"""

    def test_file_storage_no_args(self):
        """Test for file_storage"""
        self.assertIsInstance(models.storage, FileStorage)
        self.assertEqual(models.storage.__class__.__name__, "FileStorage")
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertIsInstance(models.storage._FileStorage__objects, dict)

    def test_FileStorage_with_args(self):
        """Test for file_storage with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

        def test_storage_init(self):
            """Test storage variables as instance"""
            self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """Test for file_storage.py"""

    def setUp(self):
        """Set up for test"""
        self.test_file = "file.json"

    def tearDown(self):
        """Tear down for test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_dict(self):
        """Test all method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test new method"""
        new = BaseModel()
        models.storage.new(new)
        self.assertIn("BaseModel.{}".format(new.id), models.storage.all())

    def test_new_args(self):
        """Test new method with args"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_none(self):
        """Test new method with None"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_reload(self):
        """Test save and reload method"""
        new1 = BaseModel()
        new2 = BaseModel()
        models.storage.new(new1)
        models.storage.new(new2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = "BaseModel.{}".format(new1.id)
        result = new_storage.all().get(key)
        self.assertTrue(result is not None)

        key = "BaseModel.{}".format(new2.id)
        self.assertTrue(new_storage.all().get(key) is not None)

    def test_save_file(self):
        """Test save mobjects to file"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(
            os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_file_empty(self):
        """test reload from empty file"""
        with self.assertRaises(TypeError):
            models.storage.reload()


if __name__ == "__main__":
    unittest.main()
