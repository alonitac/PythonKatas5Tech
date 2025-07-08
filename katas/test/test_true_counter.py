import unittest
from katas.true_counter import count_true_values


class TestTrueCounter(unittest.TestCase):
    def test_true_count(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_empty_list(self):
        self.assertEqual(count_true_values([]), 0)

    def test_no_true_values(self):
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_all_true_values(self):
        self.assertEqual(count_true_values([True, True, True]), 3)


