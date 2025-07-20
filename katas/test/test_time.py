import unittest
import time
from katas.time_me import measure_execution_time

class TestMeasureExecutionTime(unittest.TestCase):

    def test_sleep_100ms(self):
        def sleep_function():
            time.sleep(0.1)

        duration = measure_execution_time(sleep_function)
        # Allow a margin of error due to OS timing variations
        self.assertTrue(90 <= duration <= 200, f"Duration was {duration} ms")

    def test_instant_function(self):
        def quick_function():
            return sum([i for i in range(1000)])

        duration = measure_execution_time(quick_function)
        self.assertTrue(duration >= 0)