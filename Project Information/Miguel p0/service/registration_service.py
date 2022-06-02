from models.login_dto import Login
from models.user_info_dto import User


def validate_registration(input):
    login_dto = Login(0, input.get("username"), input.get("password"))
    info_dto = User(0, input.get("email"), input.get("first_name"), input.get("last_name"))
    pass

