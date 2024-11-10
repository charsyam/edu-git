import pytest

from add import add


def test_add_true():
    assert add(1, 2) == 3
    assert add(2, 3) == 5


def test_add_false():
    assert add(4, 4) != 3
