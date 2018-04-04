from psycopg2 import connect

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'exercises_db'


def insert_product(cursor, product):
    sql = '''
        INSERT INTO product VALUES (DEFAULT, '{}', '{}', {});
    '''.format(product['name'], product['description'], product['price'])
    cursor.execute(sql)


def insert_order(cursor, order):
    sql = '''
        INSERT INTO orderx VALUES (DEFAULT, '{}');
    '''.format(order['description'])
    cursor.execute(sql)


def insert_client(cursor, client):
    sql = '''
        INSERT INTO client VALUES (DEFAULT, '{}', '{}');
    '''.format(client['name'], client['surname'])
    cursor.execute(sql)


cnx = connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    database=DB_NAME
)
cnx.autocommit = True
cursor = cnx.cursor()

insert_product(cursor, {'name': 'Mleko', 'description': 'mleko z krowy 2%', 'price': 2.5})
insert_product(cursor, {'name': 'Mleko', 'description': 'mleko z krowy 5%', 'price': 2.7})
insert_order(cursor, {'description': 'no siema'})
insert_client(cursor, {'name': 'Tomy', 'surname': 'Lee Jones'})

cursor.close()
cnx.close()