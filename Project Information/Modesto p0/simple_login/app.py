# I will run flask here

from flask import Flask, render_template, request
from database.login_dao import insert_user, select_user, delete_user
from models.login_dto import Login
from controller.home_controller import *
from controller.login_controller import *
from controller.registration_controller import *
from controller.delete_controller import *
from controller.dashboard_controller import *
# import logging
# import os
# from logging.config import dictConfig

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

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

@app.route('/dashboard')
def dashboard_page():
    return get_dashboard()

@app.route('/dashboard/deposit', methods=["POST"])
def deposit_into_account():
    return deposit_action(request.form)

@app.route('/dashboard/withdraw', methods=["POST"])
def withdraw_from_account():
    return withdraw_action(request.form)

@app.route('/dashboard/send', methods=["POST"])
def send_to_account():
    return send_action(request.form)


# @app.route("/")
# def main():
#     app.logger.debug("debug")
#     app.logger.info("info")
#     app.logger.warning("warning")
#     app.logger.error("error")
#     app.logger.critical("critical")
#     return ""


if __name__ == "__main__":
    app.run(debug=True)