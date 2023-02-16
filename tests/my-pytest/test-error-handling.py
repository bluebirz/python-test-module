import sys
import os
import pytest
import re

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(parent_dir)
from src import main


def test_adder_with_error_handling_by_raise_err_check_type_only():
    with pytest.raises(Exception) as exc:
        result = main.adder_with_error_handling(2, 0)
    assert exc.type == ValueError


def test_adder_with_error_handling_by_raise_err_check_type_and_msg():
    checker = re.compile("higher.*zero")
    with pytest.raises(Exception) as exc:
        result = main.adder_with_error_handling(2, -1)
    assert checker.search(str(exc.value).lower()) is not None
