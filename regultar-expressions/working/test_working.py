import pytest
from working import convert


def test_period():
    with pytest.raises(ValueError):
        convert("8:00 to 12:00")

def test_to():
    with pytest.raises(ValueError):
        convert("8:00 AM - 12:00 PM")
        convert("8 AM - 12 PM")
        convert("8:00 AM - 12 PM")
        convert("8 AM - 12:00 PM")


def test_hours():
    with pytest.raises(ValueError):
        convert("10 AM to 13 PM")
        convert("20 PM to 10 AM")
        convert("13:00 PM to 18:00 PM")


def test_minutes():
    with pytest.raises(ValueError):
        convert("8:60 AM to 9:00 PM")
        convert("8:00 AM to 12:60 PM")


def test_format():
    assert convert("10 AM to 9:00 PM") == "10:00 to 21:00"
    assert convert("10 AM to 9 PM") == "10:00 to 21:00"
    assert convert("10:00 AM to 9 PM") == "10:00 to 21:00"
    assert convert("10:00 AM to 9:00 PM") == "10:00 to 21:00"