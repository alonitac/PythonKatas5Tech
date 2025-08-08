import unittest
from katas.find_missing_number import find_missing_number

class TestFindMissingNumber(unittest.TestCase):

    def test_empty_arr(self):
        arr=[]
        self.assertEqual(find_missing_number(arr), 0)

    def test_valid_email(self):
        arr=[9, 6, 4, 2, 3, 5, 7, 0, 1]
        self.assertEqual(find_missing_number(arr), 8)
    
    