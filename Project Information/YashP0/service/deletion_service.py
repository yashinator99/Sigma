from repository.login_dao import get_user_id, delete_user
from repository.user_info_dao import delete_user_info
from repository.request_dao import delete_user_request

def prep_user_id(registration_input):
    user_id = get_user_id(registration_input)

    if user_id is not None:
        return user_id

def delete_user_from_db(user_id):
    delete_user_request(user_id)
    delete_user_info(user_id)
    delete_user(user_id)


