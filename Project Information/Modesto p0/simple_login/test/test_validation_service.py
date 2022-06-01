from service.validation_service import *
import pytest

@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....", False), ("Brian", True), ("Tom", True),
    ("sasddaksjdghaskjgdfksakdsajfks", False),
    ("                   dsfdsfjksdh", False),
    ("2345656", False), ("asds sadfds", False)
))
def test_validate_first_name(test_name, expected):
    assert validate_first_name(test_name) == expected

@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....", False), ("Brian", True), ("Tom", True),
    ("sasddaksjdghaskjgdfksakdsajfks", False),
    ("                   dsfdsfjksdh", False),
    ("2345656", False), ("asds sadfds", False)
))
def test_validate_last_name(test_name, expected):
    assert validate_last_name(test_name) == expected

@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....", False), ("Brian", True), ("Tom", True),
    ("sasddaksjdghaskjgdfksakdsajfks", False),
    ("                   dsfdsfjksdh", False),
    ("2345656", False), ("asds sadfds", False)
))
def test_validate_username(test_name, expected):
    assert validate_username(test_name) == expected

@pytest.mark.parametrize("test_name, expected", (
    ("A", False), (" ", False), (".....", False), ("Brian", True), ("Tom", True),
    ("sasddaksjdghaskjgdfksakdsajfks", False),
    ("                   dsfdsfjksdh", False),
    ("2345656", False), ("asds sadfds", False)
))
def test_validate_password(test_name, expected):
    assert validate_password(test_name) == expected