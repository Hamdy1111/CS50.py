import pytest
from fuel import convert, gauge

def test_convert():
    # Test valid inputs
    assert convert("3/5") == 60
    assert convert("1/2") == 50

    # Test ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

    # Test ValueError
    with pytest.raises(ValueError):
        convert("6/5")

def test_gauge():
    # Test valid inputs
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(42) == "42%"

    # Add more tests for different cases

def test_main(capsys, monkeypatch):
    # Test input and output
    monkeypatch.setattr('builtins.input', lambda _: '3/5\n')
    #main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "60%"

    # Add more tests for different cases

if __name__ == "__main__":
    pytest.main()
