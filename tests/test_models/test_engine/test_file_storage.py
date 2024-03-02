import json
import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self) -> None:
        self.file_storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self) -> None:
        try:
            os.remove(self.file_storage._FileStorage__file_path)
            self.file_storage._FileStorage__objects.clear()
        except IOError:
            pass

    def test_new(self):
        self.file_storage.new(self.model)
        self.assertIn('BaseModel.' + self.model.id, self.file_storage.all())

    def test_save(self):
        self.file_storage.new(self.model)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))

        with open(self.file_storage._FileStorage__file_path) as f:
            data = json.load(f)
            self.assertIn('BaseModel.' + self.model.id, data)

    def test_reload(self):
        self.file_storage.new(self.model)
        self.file_storage.save()
        self.file_storage._FileStorage__objects = {}
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))
        self.file_storage.reload()
        self.assertIn('BaseModel.' + self.model.id, self.file_storage._FileStorage__objects)

    def test_file_path(self):
        self.file_storage.new(self.model)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_storage._FileStorage__file_path))
