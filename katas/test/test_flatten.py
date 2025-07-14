import unittest
from katas.list_flatten import flatten_list
class TestFlattenList(unittest.TestCase):

    def test_flat_list(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_single_level_nesting(self):
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_multi_level_nesting(self):
        self.assertEqual(flatten_list([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_all_empty_nested_lists(self):
        self.assertEqual(flatten_list([[], [[]], [[], [[]]]]), [])

    def test_deeply_nested_single_value(self):
        self.assertEqual(flatten_list([[[[[5]]]]]), [5])

    def test_mixed_values(self):
        self.assertEqual(flatten_list([1, [2, [], [3]], 4]), [1, 2, 3, 4])
