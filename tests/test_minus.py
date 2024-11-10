import pytest

from minus import minus


def test_minus_true():
    assert minus(1, 2) == -1
    assert minus(2, 3) == -1
    assert minus(3, 3) == 0

def test_minus_false():
    assert minus(4, 4) != 2
