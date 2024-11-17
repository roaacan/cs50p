import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(10)
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
        jar.withdraw(10)


def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"
