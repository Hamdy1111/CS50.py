from bank import value

def test_assert():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("How'er you") == 20
    assert value("welcome") == 100
    assert value("WALCOME") == 100
