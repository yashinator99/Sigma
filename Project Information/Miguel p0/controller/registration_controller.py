from flask import render_template

def get_registration_page():
    return render_template("registration.html")

def register_user(register_input):
    # validate input
    return register_input