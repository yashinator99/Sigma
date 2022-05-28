# I will run flask here

from flask import Flask, render_template, request
from database.login_dao import insert_user, select_user, delete_user
from models.login_dto import Login
from controller.home_controller import *
from controller.login_controller import *
from controller.registration_controller import *
from controller.delete_controller import *


app = Flask(__name__)

@app.route('/', methods=["GET"])
def landing_page():
    return get_homepage()

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()

@app.route('/login/input', methods=["POST"])
def user_login():
    return check_user_login(request.form)

@app.route('/registration')
def registration_page():
    return get_registration_page()

@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)

@app.route('/deletion', methods=["GET"])
def deletion_page():
    return get_deletion_page()

@app.route('/deletion/input', methods=["POST"])
def delete_existing_user():
    return delete_user(request.form)

if __name__ == "__main__":
    app.run(debug=True)