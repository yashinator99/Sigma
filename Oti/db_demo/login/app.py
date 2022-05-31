from flask import Flask, redirect, render_template, request, session, url_for

from database.login_dao import insert_user
from database.login_dao import select_user
from models.login_dto import Login
# Run Flask here


app = Flask(__name__)

@app.route('/', methods=["GET"])
def landing_page():
    return render_template("index.html")

@app.route('/login', methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route('/login/input', methods=["POST"])
def validate_login():
    login_input = request.form 
    print(login_input)
    user_dto = select_user(login_input.get("username"), login_input.get("password"))
    if user_dto is None:
        return "Failed Login"
    else:
        return render_template("account_page.html")

    

if __name__ == "__main__":
    app.run(debug=True)