from psycopg2 import connect

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'


cnx = connect(
    user=USER,
    password=PASSWORD,
    host=HOST
)
cnx.autocommit = True
cursor = cnx.cursor()



sql = """

CREATE DATABASE cinemas_db;   
"""

cursor.execute(sql)

cursor.close()
cnx.close()


def get_connection():
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database='exercises_db')   # funkcja tworzy polaczenie do bazy
    cnx.autocommit = True
    return cnx


cnx = get_connection()
cursor = cnx.cursor()
# Tutaj robimy zapytania.które wykonuja sie na bazie exercises_db

sql = """
    CREATE TABLE cinema (
        id SERIAL, 
        name VARCHAR(255),
        adress VARCHAR(255),
        PRIMARY KEY(id)
        );
"""
cursor.execute(sql)

sql = """
    CREATE TABLE movie (
    id SERIAL,
    name VARCHAR(255),
    description TEXT,
    PRIMARY KEY(id)
    );
"""
cursor.execute(sql)

sql = """
    CREATE TABLE ticket (
    id SERIAL,
    quantity INTEGER,
    price REAL,
    PRIMARY KEY(id)
    );
"""
cursor.execute(sql)


sql = """
    CREATE TABLE payment (
    id SERIAL,
    type_payment TEXT,
    date DATE, 
    PRIMARY KEY(id)
    );
"""
cursor.execute(sql)

cursor.close()
cnx.close