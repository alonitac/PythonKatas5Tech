import unittest
from katas.list_flatten import flatten_list


class TestListFlatten(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(flatten_list([[],[]]),[])

    def test_nested_arr(self):
        self.assertEqual(flatten_list([1,[2, 3],[4, [5, 6]],7]),[1,2,3,4,5,6,7])

    def test_regular_arr(self):
        self.assertEqual(flatten_list([1,2,3]),[1,2,3])

        
    