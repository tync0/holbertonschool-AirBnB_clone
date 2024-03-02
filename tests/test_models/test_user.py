import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """ Set up any objects, fixtures, etc. before the tests run """
        self.user = User()

    def test_email(self):
        """ Test User email """
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")

    def test_password(self):
        """ Test User password """
        self.user.password = "password123"
        self.assertEqual(self.user.password, "password123")

    def test_first_name(self):
        """ Test User first name """
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name(self):
        """ Test User last name """
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()

