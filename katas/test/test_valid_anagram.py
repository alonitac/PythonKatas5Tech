import unittest
from katas.valid_anagram import is_anagram


class TestValidAnagram(unittest.TestCase):
    def test_empty_Strs(self):
        self.assertEqual(is_anagram('',''), True)

    def test_empty_Str(self):
        self.assertEqual(is_anagram('hello',''), False)

    def test_no_true_values(self):
        self.assertEqual(is_anagram('My Name','Tameer'), 0)

    def test_true_values(self):
        self.assertEqual(is_anagram('AbCdEfG','gFeDcBa'), True)


