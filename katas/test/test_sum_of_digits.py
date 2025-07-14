import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(sum_of_digits(""),0)
    
    def test_no_numbers(self):
        self.assertEqual(sum_of_digits("abcd"),0)
    
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("1a2b3c4d -1"),11)