import pytest
from fuel import convert, gauge


def test_convert_fraction():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_convert_str():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_division_zero():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
