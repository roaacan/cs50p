from plates import is_valid


def test_length():
    assert is_valid("AB") == True
    assert is_valid("AAABBB") == True
    assert is_valid("X") == False
    assert is_valid("XXXYYYA") == False


def test_starts_two_letters():
    assert is_valid("ABC") == True
    assert is_valid("121") == False
    assert is_valid("A1") == False


def test_numbers():
    assert is_valid("AA332") == True
    assert is_valid("AB50") == True
    assert is_valid("AB50A") == False


def test_start_with_zero():
    assert is_valid("AA012") == False
    assert is_valid("AB10") == True


def test_special_characters():
    assert is_valid("AA.2") == False
    assert is_valid("AA?!") == False
    assert is_valid("AB,CD") == False
