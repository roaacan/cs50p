import pytest
from convert import convert


def test_conversation():
    assert convert(1) == 149597870700
    assert convert(5) == 747989353500


def test_error():
    with pytest.raises(TypeError):
        convert("1")


def test_float_conversation():
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
    assert (7/3) == pytest.approx(2.4, abs=0.1) # Aproximar resultados con pytest