import unittest
from katas.time_me import measure_execution_time, sample_function, quick_function


class TestTimeMe(unittest.TestCase):
    def test_sample_function(self):
        # Test the execution time of sample_function
        self.assertAlmostEqual(measure_execution_time(sample_function), 500, delta=50)

    def test_quick_function(self):
        # Test the execution time of quick_function
        self.assertLess(measure_execution_time(quick_function), 1)


    

