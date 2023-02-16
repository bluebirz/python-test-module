import unittest
import sys, os
import logging

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)
from src import main

logging.basicConfig(stream=sys.stdout)
logname = "test-multiple-logging"
logging.getLogger(logname).setLevel(logging.DEBUG)
log = logging.getLogger(logname)


class TestMyFunctions(unittest.TestCase):
    def test_adder_simple_by_both_positive(self):
        log.debug(self._testMethodName)
        self.assertEqual(main.adder_simple(1, 1), 2)
        self.assertEqual(main.adder_simple(2, 2), 4)

    def test_adder_simple_by_both_negative(self):
        log.debug(self._testMethodName)
        self.assertEqual(main.adder_simple(-1, -1), -2)
        self.assertEqual(main.adder_simple(-2, -2), -4)

    def test_adder_simple_by_pos_and_neg(self):
        log.debug(self._testMethodName)
        self.assertEqual(main.adder_simple(-2, 2), 0)
        self.assertEqual(main.adder_simple(3, -5), -2)


if __name__ == "__main__":
    unittest.main()
