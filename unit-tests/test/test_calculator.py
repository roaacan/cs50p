import pytest
from calculator import square


def test_square_zero():
    assert square(0) == 0


def test_square_negative():
    assert square(-1) == 1
    assert square(-10) == 100


def test_square_positive():
    assert square(4) == 16
    assert square(5) == 25


def test_square_str():
    with pytest.raises(TypeError):
        square("cat")
        square("-1")