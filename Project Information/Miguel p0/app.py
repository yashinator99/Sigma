from flask import Flask, request
#from database.login_dao import insert_address, insert_user, select_user
from controller.home_controller import get_homepage
from controller.login_controller import get_login_page, check_user_login
from controller.registration_controller import get_registration_page, register_user

#def main():
    #insert_user("wayne","As!123456")
    #insert_address(1,'WayneGretzky@oilers.ca', 'Wayne', 'Gretzky', '780-414-5483', '104 Ave NW', '10220', 'Edmonton', 'Alberta', 'Canada', 'T5J 0H6')
    #print(select_user(1))

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    return get_homepage()

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()

@app.route('/login/input', methods=["POST"])
def user_login():
    return check_user_login(request.form)

@app.route('/registration', methods=["GET"])
def registration_page():
    return get_registration_page()

@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)
    
if __name__ == '__main__':
    app.run(debug=True)