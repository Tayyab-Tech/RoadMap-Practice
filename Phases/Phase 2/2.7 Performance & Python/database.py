import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="python_store",
        user="postgres",
        password="password"
    )