import unittest
from katas.list_diff import find_difference

class TestFindDifference(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find_difference([1, 2, 3, 4, 5]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_difference([-10, -20, -30]), 20)

    def test_mixed_numbers(self):
        self.assertEqual(find_difference([-10, 0, 10]), 20)

    def test_all_same(self):
        self.assertEqual(find_difference([5, 5, 5]), 0)

    def test_two_elements(self):
        self.assertEqual(find_difference([100, 5]), 95)

if __name__ == '__main__':
    unittest.main()
