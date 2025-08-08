import unittest
from katas.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(two_sum([],8), [])

    def test_no_sum(self):
        self.assertEqual(two_sum([1,2,3],9), [])

    def test_sum(self):
        self.assertEqual(two_sum([1,8,4,7,2],6), [2,4])



