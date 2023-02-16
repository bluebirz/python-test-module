import sys, os

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)

from src import main


def test_adder_simple_by_both_positive():
    assert main.adder_simple(1, 1) == 2
    assert main.adder_simple(2, 2) == 4


def test_adder_simple_by_both_negative():
    assert main.adder_simple(-1, -1) == -2
    assert main.adder_simple(-2, -2) == -4


def test_adder_simple_by_pos_and_neg():
    assert main.adder_simple(-2, 2) == 0
    assert main.adder_simple(3, -5) == -2
