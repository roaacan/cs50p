import pytest
from seasons import str_to_date, minutes_to_words


def test_input():
    with pytest.raises(ValueError):
        str_to_date("January 11, 2005")
        str_to_date("11/16/2024")


def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_words(527040) == "Five hundred twenty-seven thousand forty minutes"