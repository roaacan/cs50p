from um import count


def test_words():
    assert count("umbrella") == 0
    assert count("The umbrella is nice.") == 0


def test_puctuaction_marks():
    assert count("Um! That was amazing!") == 1
    assert count("Um, I fogot") == 1
    assert count("Um... I dunno.") == 1
