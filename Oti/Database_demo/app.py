from datetime import timedelta
from flask import Flask, request, jsonify, session
from flask import url_for
from controller.home_controller import get_homepage
from controller.login_controller import check_user_login, get_login_page
from controller.register_controller import get_registration_page, register_user



app = Flask(__name__)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

@app.route('/', methods=["GET"])
def home_page():
     return get_homepage()

@app.route('/registration', methods=["GET"])
def registration_page():
    return get_registration_page()

@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)

@app.route('/login/input', methods=["POST"])
def user_login():
    return check_user_login(request.form)

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()


@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id', None)
    return "message' : 'you successfully logged out"







# with app.test_request_context():
#     print(url_for("home_page"))
#     print(url_for("register"))
#     print(url_for("register", next='/'))
#     print(url_for("login"))
#     print(url_for("login", next='/'))
#     print(url_for("logout"))
#     print(url_for("logout", next='/'))
#     print(url_for("static", filename="style.css"))


if __name__ == "__main__":
    app.run(debug=True)