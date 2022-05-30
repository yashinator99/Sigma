from flask import render_template
from service.registration_service  import create_login,create_user_info,validate_registration

def get_registration_page():
    return render_template("registration.html")

def register_user(register_input):
    if validate_registration(register_input):
        user_id = create_login(register_input)
        info_id = create_user_info(user_id, register_input)
        if info_id is not None:
            return render_template("login.html")
    else:
        return render_template("failed_validation.html")


