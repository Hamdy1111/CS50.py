import pytest
from fuel import convert,gauge

def test_convert():
    assert convert("3/5")==60
    assert convert("1/2")==50
    assert convert("1/6")==17
def test_gauge():
    assert gauge(100)=='F'
    assert gauge(99)=='F'
    assert gauge(55)=='55%'
    assert gauge(0)=='E'
    assert gauge(1)=='E'
def test_zeroDomin():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_valueError():
    with pytest.raises(ValueError):
        convert("8/2")
