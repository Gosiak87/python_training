from psycopg2 import connect      # psycopg2 sterownik PostgreSQL dla Python

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'

# tworzenie połączenia z bazą danych
cnx = connect(           # obiekt klasy connection
    user=USER,
    password=PASSWORD,
    host=HOST
)
cnx.autocommit = True
cursor = cnx.cursor()    # odpytywanie obiektu curosor
# cursor to obiekt klasy cursor, przez który wysyła sie zapytania,



# sql = """
#
# CREATE DATABASE exercises_db;
# """
#
# # cursor.execute(sql)     zakomentowane bo wywala blad ze juz zrobilam baze

cursor.close()
cnx.close()   # zamknięcie połączenia


def get_connection():
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database='exercises_db')   # funkcja tworzy polaczenie do bazy
    cnx.autocommit = True
    return cnx


cnx = get_connection()
cursor = cnx.cursor()
# Tutaj robimy zapytania.które wykonuja sie na bazie exercises_db

sql = """
    CREATE TABLE product (
        id SERIAL, 
        name VARCHAR(255),
        description TEXT,
        price DECIMAL(5,2),
        PRIMARY KEY(id)
        );
"""
cursor.execute(sql)

sql = """
    CREATE TABLE order (
    id SERIAL,
    description TEXT,
    PRIMARY KEY(id)
    );
"""
cursor.execute(sql)

sql = """
    CREATE TABLE client (
    id SERIAL,
    name VARCHAR(100),
    surname VARCHAR(150),
    PRIMARY KEY(id)
    );
"""
cursor.execute(sql)

cursor.close()
cnx.close