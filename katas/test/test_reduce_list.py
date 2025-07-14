import unittest
from katas.reduce_list import reduce_array

class TestReduceArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(reduce_array([]),[])

    def test_one_element_array(self):
        self.assertEqual(reduce_array([1]),[1])
    
    def test_reduce_list(self):
        self.assertEqual(reduce_array([1,45,7,12,10,3]),[1,44,-38,5,-2,-7])
