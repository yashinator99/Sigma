from service.validation_service import *
import pytest

@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False), 
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False), 
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", True)
))
def test_validate_first_name(test_name, expected):
    assert validate_first_name(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False), 
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False), 
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", True)
))
def test_validate_last_name(test_name, expected):
    assert validate_last_name(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False), 
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False), 
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", True), ("Smith12", True), ("Tom1234", True), ("Thomas1234", False)
))
def test_validate_username(test_name, expected):
    assert validate_username(test_name) == expected

@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False), 
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False), 
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", False), ("Smiths1255", True), ("Tierny123", True), ("Thomas1234", True)
))
def test_validate_password(test_name, expected):
    assert validate_password(test_name) == expected