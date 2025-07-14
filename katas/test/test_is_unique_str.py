import unittest
from katas.is_unique_str import is_unique
# The test case
class TestIsUnique(unittest.TestCase):
    def test_unique_string(self):
        self.assertTrue(is_unique("abcd"))
    
    def test_non_unique_string(self):
        self.assertFalse(is_unique("aabc"))
    
    def test_case_sensitive(self):
        self.assertTrue(is_unique("Aa"))  

    def test_empty_string(self):
        self.assertTrue(is_unique(""))

    def test_single_character(self):
        self.assertTrue(is_unique("x"))