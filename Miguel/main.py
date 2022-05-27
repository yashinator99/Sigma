from connection import get_connection

def main():
    connection = get_connection
    select_query = "SELECT * FROM user_table;"

    cursor = connection.cursor()

    try:
        cursor.execute(select_query)
        print("Executing SELECT query")
        while True:
            record = cursor.fetchone()
            print(record)

            if record == None:
                break
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
if __name__ == '__main__':
    main()