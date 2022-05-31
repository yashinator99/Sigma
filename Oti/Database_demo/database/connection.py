import psycopg2

# Used to define function to get database

def get_connection():
    connection=psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Password4321",
        host="first-demo-database.ccxffernk34y.us-east-2.rds.amazonaws.com",
        port="5432"
    )
    return connection