import unittest
from katas.email_validator import is_valid_email

class TestEmailValidator(unittest.TestCase):

    def test_empty_email(self):
        email=""
        self.assertEqual(is_valid_email(email), False)

    def test_valid_email(self):
        email="asdd?asd@asd.asd"
        self.assertEqual(is_valid_email(email), True)
    
    def test_invalid_email(self):
        email="asdd@asd@asd.asd"
        self.assertEqual(is_valid_email(email), False)
    