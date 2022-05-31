from flask import render_template
from service.login_service import check_login

def get_login_page():
    return render_template("login.html")

def check_user_login(login_input):
    user_login = check_login(login_input)

    if user_login is None:
        return "Failed Login"
    else:
        return render_template("dashboard.html", username=user_login.username)