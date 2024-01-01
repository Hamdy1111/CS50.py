from numb3rs import validate


def test_valid_ipv4():
    assert validate("192.168.1.1") is True
    assert validate("10.0.0.1") is True
    assert validate("172.16.0.1") is True


def test_invalid_ipv4():
    assert validate("275.3.6.28") is False
    assert validate("192.168.300.1") is False
    assert validate("abc.def.ghi.jkl") is False


def test_edge_cases():
    assert validate("") is False
    assert validate("192.168.1") is False
    assert validate("192.168.1.1.1") is False

