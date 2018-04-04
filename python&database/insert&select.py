from psycopg2.extras import RealDictCursor
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
cursor = cnx.cursor(cursor_factory=RealDictCursor)

sql = '''
INSERT INTO users VALUES (DEFAULT, 'Jacek', 'jacek2@gmail.com') RETURNING user_id;
'''
cursor.execute(sql)
print(cursor.fetchone())

sql = '''
INSERT INTO users(user_name, user_email) VALUES('Wojtek', 'wojtek2@gmail.com') RETURNING *;
'''
cursor.execute(sql)
print(cursor.fetchone())


#Metoda execute w przypadku udanych zapytań SELECT, zwraca nam iterator.

#Aby dostać się do danych zawróconych przez zapytanie, należy przeiterować się przez obiekt cursor:

cursor.execute('''SELECT user_name, user_email FROM users;''')
print(cursor.fetchall())
for row in cursor:
    print(row)

cursor.execute('''SELECT * FROM users WHERE user_name = 'Wojtek';''')
users = cursor.fetchall()
print('Dostaliśmy {} rekordów'.format(len(users)))
for row in cursor:
    print(row)


cursor.close()
cnx.close()


