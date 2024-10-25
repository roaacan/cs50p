from hello import hello


def test_hello_default():
    assert hello() == "hello, world"


def test_hello_input():
    assert hello("Juan") == "hello, Juan"