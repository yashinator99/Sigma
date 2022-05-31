from datetime import timedelta
from flask_cors import CORS
from flask import Flask, jsonify, render_template, request, session

import psycopg2 
import psycopg2.extras
from controller.registration_controller import get_registration_page, register_user

from models.login_dto import Login 


app = Flask(__name__)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
CORS(app)


DB_HOST="first-demo-database.ccxffernk34y.us-east-2.rds.amazonaws.com"
DB_NAME="postgres"
DB_USER="postgres"
DB_PASS="Password4321"
DB_PORT="5432"

conn = psycopg2.connect(host=DB_HOST, dbname=DB_USER, port=DB_PORT, user=DB_USER, password=DB_PASS )


@app.route('/', methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route('/input/input')
def session_check():
    if 'username' in session:
        username = session['username']
        return jsonify({'message' : 'You are already logged in', 'username' : username})
    else:
        resp = jsonify({'message' : 'Unauthorized'})
        resp.status_code = 401
        return resp

@app.route('/input', methods=['POST'])
def login():
    _json = request.json
    _username = _json['username']
    _password = _json['password']

    #validate the received Values
    if _username and _password:
        # check if user exists
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        qry = "SELECT * FROM user_table WHERE username=%s"
        qry_where = (_username,)

        cursor.execute(qry, qry_where)
        row = cursor.fetchone()
        username = row['username']
        password = row['password']
        if row:
            if password:
                session['username'] = username 
                cursor.close()
                return jsonify({'message' : 'You are logged in successfully'})
            else:
                resp = jsonify({'message' : 'Bad Request - invalid password'})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({'message' : 'Bad Request - invalid credentials'})
            resp.status_code = 400
            return resp


@app.route('/registration', methods=["GET"])
def registration_page():
    return get_registration_page()


@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)
    


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return jsonify({'message' : 'you successfully logged out'})


if __name__ == "__main__":
    app.run()

