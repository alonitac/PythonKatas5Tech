import unittest
from katas.true_counter import true_counter


class TestTrueCounter(unittest.TestCase):
    def test_true_count(self):
        self.assertEqual(true_counter([True, False, True, True, False]), 3)

    def test_empty_list(self):
        self.assertEqual(true_counter([]), 0)

    def test_no_true_values(self):
        self.assertEqual(true_counter([False, False, False]), 0)

    def test_all_true_values(self):
        self.assertEqual(true_counter([True, True, True]), 3)


