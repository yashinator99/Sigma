import psycopg2

def get_connection():
    connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="Piplup!6",
            host="p0-database.cvzbvdn4nh5s.us-west-1.rds.amazonaws.com",
            port="5432"
            )
    return connection

