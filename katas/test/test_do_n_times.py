import unittest
from unittest.mock import Mock
from katas.do_n_times import do_n_times,addCnt


class TestDoNTimes(unittest.TestCase):

    def test_do_n_times_calls_function_correctly(self):
        mock_func = Mock()

        do_n_times(mock_func, 5)

        # Assert it was called exactly 5 times
        self.assertEqual(mock_func.call_count, 5)