import psycopg2

def get_connection():
    connection = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "yqX78Q7V1r9FNoT0YFyH",
        host = "database-p0.cr3sz4iayjew.us-east-2.rds.amazonaws.com",
        port = "5432"
    )

    return connection