from repository.connection import get_connection
from models.login_dto import Login
import psycopg2
# DAO = Data Access Object

def select_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0], record[1], record[2])
            return user_login
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM users WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0], record[1], record[2])
            return user_login
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO users VALUES (default, %s, %s) RETURNING user_id;"

    try:
        cursor.execute(qry, (username, password))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def insert_address(id, email, first_name, last_name, phone_number, address_1, address_2, city, state, country, zip_code):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO address VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    try:
        cursor.execute(qry, (id, email, first_name, last_name, phone_number, address_1, address_2, city, state, country, zip_code))
        connection.commit()
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

    