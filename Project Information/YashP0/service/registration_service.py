from models.login_dto import Login
from models.user_info_dto import User
from repository.login_dao import insert_user, select_user_by_id
from repository.user_info_dao import insert_user_info
# To register
# Valid Username and Password
# Valid first name and last name

def validate_registration(input):
    login_dto = Login(0, input.get("username"), input.get("password"))
    info_dto = User(0, 0, input.get("first_name"), input.get("last_name"), input.get("email"))
    return login_dto.validate_login() and info_dto.validate_user_info()

    #if (login_dto.validate_login() and info_dto.validate_user_info()):
    #    pass
    #else:
    #    return None
def create_login(registration_input):
    user_id = insert_user(registration_input.get("username"), registration_input.get("password"))

    if user_id is not None:
        return user_id

def create_user_info(user_id, registration_input):
    login_dto = select_user_by_id(user_id)
    info_id = insert_user_info(login_dto, registration_input.get("first_name"),registration_input.get("last_name"),registration_input.get("email"))
    if info_id is not None:
        return info_id
