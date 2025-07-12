import unittest
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):

    def test_unique_string(self):
        self.assertTrue(is_unique('World'))
    
    def test_not_unique(self):
        self.assertFalse(is_unique('Hello'))
    