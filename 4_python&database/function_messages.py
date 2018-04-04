
#Napisz funkcję messages(id), która zwróci wszystkie wiadomości (listę wiadomości,
# nie cały zestaw danych z tabeli) dla użytkownika o identyfikatorze przekazanym jako parametr funkcji.
# Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.


from psycopg2 import connect

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'exercises_db'

cnx = connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    database=DB_NAME
)
cnx.autocommit = True
cursor = cnx.cursor()


def messages(id):
    sql = '''
        SELECT * FROM messages WHERE user_id = {};
    '''.format(messages['user_id'])
    cursor.execute(sql)
    return cursor.fetchall()


cursor.close()
cnx.close()


