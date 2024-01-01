from um import count



def test_single_occurrence():
    assert count("Hello, um, world!") == 1
    assert count("Um, this is a test.") == 1


def test_multiple_occurrences():
    assert count("Um, um, um, testing!") == 3
    assert count("um um um") == 3


def test_no_occurrence():
    assert count("Yummy") == 0
    assert count("The quick brown fox") == 0
