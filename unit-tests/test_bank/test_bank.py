from bank import value


def test_hello():
    assert value("hello, world") == 0
    assert value("Hello, world") == 0
    assert value("HELLO, WORLD") == 0


def test_start_with_h():
    assert value("Hey, world") == 20
    assert value("hey, world") == 20
    assert value("HEY WORLD") == 20


def test_start_without_h():
    assert value("What's up?") == 100
    assert value("what's up?") == 100
    assert value("WHAT'S UP?") == 100
