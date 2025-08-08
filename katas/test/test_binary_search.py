import unittest
from katas.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_arr(self):
        self.assertEqual(binary_search([],1), -1)

    def test_unsorted_arr(self):
        self.assertIsNot(binary_search([5,4,3,2,1],2), 3)
    
    def test_search_found(self):
        self.assertEqual(binary_search([1,4,9,26,41],26), 3)

    def test_search_not_found(self):
        self.assertEqual(binary_search([1,4,9,26,41],3), -1)
    