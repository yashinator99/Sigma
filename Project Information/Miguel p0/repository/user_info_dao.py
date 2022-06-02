import psycopg2
from repository.connection import get_connection
from models.user_info_dto import User
from models.login_dto import Login

def select_user_info_by_id(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM address WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_by_user(login_dto: Login):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM users WHERE user_id = '{login_dto.user_id}';"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_address(login_dto: Login, email, first_name, last_name, phone_number, address_1, address_2, city, state, country, zip_code):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO address VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING user_id;"

    try:
        cursor.execute(qry, (login_dto.user_id, email, first_name, last_name, phone_number, address_1, address_2, city, state, country, zip_code))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()