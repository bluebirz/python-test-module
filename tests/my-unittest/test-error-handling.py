import unittest
import sys
import os
import logging

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)
from src import main

# logging.basicConfig(stream=sys.stderr)
# logname = "my-unittest"
# logging.getLogger(logname).setLevel(logging.DEBUG)
# log = logging.getLogger(logname)


class TestMyFunctions(unittest.TestCase):
    # def test_adder_simple_by_both_positive(self):
    #     #     # log.debug(self._testMethodName)
    #     self.assertEqual(main.adder_simple(1, 1), 2)
    #     self.assertEqual(main.adder_simple(2, 2), 4)

    # def test_adder_simple_by_both_negative(self):
    #     # log.debug(self._testMethodName)
    #     self.assertEqual(main.adder_simple(-1, -1), -2)
    #     self.assertEqual(main.adder_simple(-2, -2), -4)

    # def test_adder_simple_by_pos_and_neg(self):
    #     # log.debug(self._testMethodName)
    #     self.assertEqual(main.adder_simple(-2, 2), 1)
    #     self.assertEqual(main.adder_simple(3, -5), -2)

    def test_adder_with_error_handling_by_raise_err(self):
        # log.debug(self._testMethodName)
        with self.assertRaisesRegex(ValueError, "higher.*zero"):
            main.adder_with_error_handling(2, -1)
            main.adder_with_error_handling(2, 0)

    def test_adder_with_error_handling_by_not_raise_err(self):
        # log.debug(self._testMethodName)
        # with self.assertRaisesRegex(ValueError, "higher.*zero"):
        self.assertEqual(main.adder_with_error_handling(2, 1), 3)
        self.assertEqual(main.adder_with_error_handling(2, 2), 4)

    # def test_adder_with_error_handling_by_should_raise_err(self):
    #     # log.debug(self._testMethodName)
    #     # with self.assertRaisesRegex(ValueError, "higher.*zero"):
    #     self.assertEqual(main.adder_with_error_handling(2, 1), 3)
    #     self.assertEqual(main.adder_with_error_handling(2, 2), 4)

    # self.assertEqual(main.adder(3, 10), )
    # self.assertEqual(main.adder(4, 0), 6)
    # self.assertEqual(main.adder(5, 88), 6)
    # self.assertEqual(main.adder(-6, 9), 6)


if __name__ == "__main__":
    unittest.main()
