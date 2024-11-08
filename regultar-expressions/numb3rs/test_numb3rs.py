from numb3rs import validate


def test_str():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False


def test_octects():
    assert validate("255") == False
    assert validate("255.172") == False
    assert validate("176.172.255") == False
    assert validate("255.255.0.1.255") == False
    


def test_range():
    assert validate("256.178.12.1") == False
    assert validate("128.256.255.0") == False
    assert validate("128.255.256.0") == False
    assert validate("171.0.0.256") == False