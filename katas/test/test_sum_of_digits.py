import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_digits_only(self):
        self.assertEqual(sum_of_digits("12345"), 15)

    def test_mixed_characters(self):
        self.assertEqual(sum_of_digits("a1b2c3"), 6)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("abcdef!@#"), 0)

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_spaces_and_digits(self):
        self.assertEqual(sum_of_digits(" 9 8 7 "), 24)