import pytest
from models.login_dto import Login
from repository.login_dao import *
from repository.request_dao import *
from repository.user_info_dao import *



def test_select_user_by_id():
    user_login = select_user_by_id(5)
    user_test = Login("5", "user_1", "pass_1")
    assert repr(user_login) ==  repr(user_test)


def test_select_user_by_id_fail1():
    user_login = select_user_by_id(10)
    user_test = Login("5", "user_1", "pass_1")
    assert repr(user_login) != repr(user_test)

def test_select_user_by_id_fail2():
    user_login = select_user_by_id(5)
    user_test = Login("6", "user_1", "pass_1")
    assert repr(user_login) != repr(user_test)



def test_select_user():
    user_login = select_user("YashKh","Password")
    user_test = Login("10", "YashKh","Password")
    assert repr(user_login) ==  repr(user_test)


def test_select_user_fail():
    user_login = select_user("YashKh","Password1")
    user_test = Login("10", "YashKh","Password")
    assert repr(user_login) !=  repr(user_test)

def test_select_user_fail2():
    user_login = select_user("YashKh","Password")
    user_test = Login("10", "YashKh","Password1")
    assert repr(user_login) !=  repr(user_test)

def test_input_user():
    insert_user("TonyStank", "Ironmanrules")
    user_login = select_user("TonyStank", "Ironmanrules")
    user_id = get_user_id("TonyStank")
    user_test = Login(str(user_id), "TonyStank", "Ironmanrules")
    assert repr(user_login) ==  repr(user_test)

def test_input_user_fail_1():
    insert_user("TonyStank", "Ironmanrules")
    user_login = select_user("TonyStank", "Ironmanrules")
    user_test = Login("11", "TonySank", "Ironmanrules")
    assert repr(user_login) !=  repr(user_test)

def test_input_user_fail_reversedpasswordusername():
    insert_user("Ironmanrules", "TonyStank")
    user_login = select_user("TonyStank", "Ironmanrules")
    user_test_the_insert_user = Login("12", "Ironmanrules", "TonyStank")
    assert repr(user_login) !=  repr(user_test_the_insert_user)

def test_get_user_id():
    assert get_user_id("YashKh") == 10

def test_get_user_id_failed():
    assert get_user_id("YashKh") != 11

def test_get_user_id_failed_2():
    assert get_user_id("YashKh") != get_user_id("test_user_1")

def test_delete_user():
    insert_user("Deleted_user", "Ironmanrules")
    id =get_user_id("Deleted_user")
    delete_user(id)
    assert id != get_user_id("Deleted_user")

def test_delete_user_fail1():
    insert_user("Deleted_user", "Ironmanrules")
    id =get_user_id("Deleted_user")
    fake_id = 15
    delete_user(fake_id)
    assert id == get_user_id("Deleted_user")

