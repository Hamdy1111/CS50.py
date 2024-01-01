import pytest
from project import check_password, check_username, signUp

def test_password():
    assert check_password("ValidP@ssword1") == True
    assert check_password("weakpassword") == False

def test_username_isfound():
    assert check_username("john_doe") == True
    assert check_username("new_user") == False

def test_signUp():
    with pytest.raises(SystemExit) as e:
        signUp("new_user", "SecureP@ss1")

    assert str(e.value) == "Sign Up Is Complete"
    
