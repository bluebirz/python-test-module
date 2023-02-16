import sys, os
import pytest

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)

from src import main

test_cases = [
    ((1, 1), 2),
    ((2, 2), 4),
    ((-1, -1), -2),
    ((-2, -2), -4),
    ((-2, 2), 0),
    ((3, -5), -2),
]


@pytest.mark.parametrize("arguments, expect", test_cases)  # decorator
def test_adder_simple(arguments, expect):
    a, b = arguments
    assert main.adder_simple(a, b) == expect


@pytest.mark.parametrize("arguments, expect", test_cases)
def test_adder_simple_unpack(arguments, expect):
    # unpack using `*collection_variable`
    assert main.adder_simple(*arguments) == expect
