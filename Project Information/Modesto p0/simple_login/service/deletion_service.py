# In order to register to my service, they need:
# Valid Username and password
# Valid first_name and Last_name
# In this case, my only validation is checking the length of each input

from models.login_dto import Login
from models.user_info_dto import User
from database.login_dao import fetch_delete_user, delete_user
from database.user_info_dao import delete_user_info


def validate_deletion(input):
    login_dto = Login(0, input.get("username"), input.get("password"))
    return login_dto.validate_login()

def fetch_delete_login(input):
    user_id = fetch_delete_user(input.get("username"), input.get("password"))

    if user_id is not None:
        return user_id

def delete_user_information(user_id):
    print(f"user_id: {user_id}")
    # Have to delete data from info_table first since the user_id is a foreign key in that table
    delete_user_info(user_id)
    delete_user(user_id)