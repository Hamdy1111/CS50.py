from working import convert
import pytest

def test_valid_formats():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 3:45 PM") == "12:30 to 15:45"

def test_invalid_formats():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("8:00 to 16:00")

    with pytest.raises(ValueError):
        convert("10:00 AM to 13:00 PM")
