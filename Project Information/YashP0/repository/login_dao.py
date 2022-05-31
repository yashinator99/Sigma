import psycopg2
from repository.connection import get_connection
from models.login_dto import Login

def select_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE user_id = {user_id};"

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

def select_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE username = '{username}' AND passwrd = '{password}';"

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

    qry = "INSERT INTO user_table VALUES (default, %s, %s) RETURNING user_id;"

    try:
        cursor.execute(qry,(username,password))
        id = cursor.fetchone()[0]
        #while True:
        #    record = cursor.fetchone()
        #    if record is None:
        #        break
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def get_user_id(username):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM user_table WHERE username = '{username}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_id = record[0]
            return user_id
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def delete_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM user_table WHERE user_id = '{user_id}';"

    try:
        cursor.execute(qry)
        connection.commit()
        return
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()
