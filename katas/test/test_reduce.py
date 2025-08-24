import unittest
from katas.reduce_list import reduce_array

class TestReduceArray(unittest.TestCase):

    def test_basic_case(self):
        nums = [10, 15, 25, 40]
        reduce_array(nums)
        self.assertEqual(nums, [10, 5, 10, 15])

    def test_single_element(self):
        nums = [42]
        reduce_array(nums)
        self.assertEqual(nums, [42])  # nothing to change

    def test_two_elements(self):
        nums = [5, 9]
        reduce_array(nums)
        self.assertEqual(nums, [5, 4])

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        reduce_array(nums)
        self.assertEqual(nums, [0, 0, 0, 0])

    def test_negative_numbers(self):
        nums = [-5, -3, -8]
        reduce_array(nums)
        self.assertEqual(nums, [-5, 2, -5])