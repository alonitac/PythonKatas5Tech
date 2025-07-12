import unittest
from katas.list_diff import find_difference


class TestListDiff(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(find_difference([]),0)

    def test_one_number(self):
        self.assertEqual(find_difference([1]),0)

    def test_list_diff(self):
        self.assertEqual(find_difference([2,4,7,8,45,1,3]),44)
        
    