#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    ''' Unittest for BaseModel class '''

    def test_object_instantiation(self):
        ''' instantiates class '''
        self.base_model = BaseModel()

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        ''' test Class: BaseModel attributes '''
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertFalse(hasattr(self.base_model, "random_attr"))
        self.assertFalse(hasattr(self.base_model, "name"))
        self.assertTrue(hasattr(self.base_model, "id"))
        self.base_model.name = "Alice"
        self.base_model.age = "44"
        self.assertTrue(hasattr(self.base_model, "name"))
        self.assertTrue(hasattr(self.base_model, "age"))
        delattr(self.base_model, "name")
        self.assertFalse(hasattr(self.base_model, "name"))
        delattr(self.base_model, "age")
        self.assertFalse(hasattr(self.base_model, "age"))
        self.assertEqual(self.base_model.__class__.__name__, "BaseModel")

    def test_save(self):
        ''' testing method: save '''
        self.base_model = BaseModel()
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_str(self):
        ''' testing __str__ return format of BaseModel '''
        self.base_model = BaseModel()
        s = "[{}] ({}) {}".format(
            self.base_model.__class__.__name__,
            str(self.base_model.id),
            self.base_model.__dict__
        )
        self.assertEqual(str(self.base_model), s)

    def test_to_dict(self):
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
