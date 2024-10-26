from twttr import shorten


def test_lower():
    assert shorten("hello world") == "hll wrld"
    assert shorten("new world") == "nw wrld"


def test_upper():
    assert shorten("HELLO WORLD") == "HLL WRLD"
    assert shorten("NEW WORLD") == "NW WRLD"


def test_number():
    assert shorten("2006") == "2006"
    assert shorten("-122") == "-122"
    assert shorten("0.1") == "0.1"


def test_punctuation():
    assert shorten("hello!") == "hll!"
    assert shorten("What is it?") == "Wht s t?"
    assert shorten("This is Rana.") == "Ths s Rn."
    assert shorten("mmm...") == "mmm..."