import unittest
from katas.do_n_times import do_n_times


class TestDoNTimes(unittest.TestCase):
    def test_n_times(self):
        counter=do_n_times(lambda: None, 5)
        self.assertEqual(counter, 5)

    def test_zero_times(self):
        counter=do_n_times(lambda: None, 0)
        self.assertEqual(counter, 0)
    
    def test_negative_times(self):
        counter=do_n_times(lambda: None, -3)
        self.assertEqual(counter, 0)