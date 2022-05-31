import pytest
from sqlalchemy import false, true
from models.login_dto import Login
from models.request_dto import Request
from models.user_info_dto import User
from service.deletion_service import *
from service.login_service import *
from service.registration_service import *
from service.request_service import *
from repository.login_dao import *
from repository.request_dao import *
from repository.user_info_dao import *

test_login = {"username":"YashKh", "password":"Password"}
test_login_fail = {"username":"YashKh", "password":"Password!!!!"}
test_login_fail_username = {"username":"Yashh", "password":"Password"}
test_request_pass_dict = {"request_title": "Hello There", "request":"General Kenobi"}
test_request_no_pass_dict = {"request_title":"Hi" , "request":"This is where the fun begins ;-)"}
test_request_no_pass_dict_2 = {"request_title":"DEW IT" , "request":"NO"}
test_registration_validation_pass = {"username":"generalkenobi", "password":"Hello There", "first_name":"Obi Wan","last_name":"Kenobi", "email":"sassmaster@gmail.com"}
test_registration_validation_fail1 = {"username":"Ash", "password":"best", "first_name":"Ash","last_name":"Ketchum", "email":"pokemonmaster@gmail.com"}
test_registration_validation_fail2 = {"username":"Ashsad", "password":"besast", "first_name":"Ash","last_name":"K", "email":"pokemonmaster@gmail.com"}
test_registration_validation_pass_2 = {"username":"supermario", "password":"peach", "first_name":"Mario","last_name":"Mario", "email":"sassmaster@gmail.com"}

def test_validate_request_service():
    flag = validate_request_service(test_request_pass_dict)
    assert flag == True

def test_validate_request_service_less_input():
    flag = validate_request_service(test_request_no_pass_dict)
    assert flag == False

def test_validate_request_service_less_input_request():
    flag = validate_request_service(test_request_no_pass_dict_2)
    assert flag != true

def test_get_view_request():
    reeequests = get_view_request(10)
    assert len(reeequests[0]) > 0

def test_get_view_request_alter():
    reeequests = get_view_request(6)
    assert len(reeequests) == 0

def test_create_request():
    #create_request(5,test_request_pass_dict)
    reeequests = get_view_request(5)
    assert test_request_pass_dict.get("request_title") == reeequests[0][1] and test_request_pass_dict.get("request") == reeequests[0][2]

def test_check_login():
    ret = check_login(test_login)
    assert ret is not None

def test_check_login_fail():
    ret = check_login(test_login_fail)
    assert ret is None

def test_check_login_fail2():
    ret = check_login(test_login_fail_username)
    assert ret is None

def test_validate_registration():
    flag = validate_registration(test_registration_validation_pass)
    assert flag == True

def test_validate_registration_fail_1():
    flag = validate_registration(test_registration_validation_fail1)
    assert flag != True

def test_validate_registration_fail_2():
    flag = validate_registration(test_registration_validation_fail2)
    assert flag != True

def test_create_login():
    user_id = create_login(test_registration_validation_pass)
    assert user_id is not None

def test_create_user_info():
    user_id = get_user_id("generalkenobi")
    id = create_user_info(user_id, test_registration_validation_pass)
    assert id is not None

def test_delete_user_from_db():
    user_id = create_login(test_registration_validation_pass_2)
    id = create_user_info(user_id, test_registration_validation_pass_2)
    delete_user_from_db(user_id)
    user_id = get_user_id("supermario")
    assert user_id is None