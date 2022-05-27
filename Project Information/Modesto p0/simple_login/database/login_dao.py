# Dao = Data Access Object
# I will limit all of my database interaction to this file
# CRUD
# Create a user login
# read a user login

import psycopg2
from database.connection import get_connection
from models.login_dto import Login



def select_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "SELECT * FROM user_table WHERE user_id = {user_id}"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            
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
        cursor.execute(qry, (username, password))
        id = cursor.fetchone()[0]
        connection.commit()
        return id

        connection.commit()
        return record
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()