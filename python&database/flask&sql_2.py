from psycopg2 import connect

from flask import Flask

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'exercises_db'

app = Flask(__name__)


@app.route("/delete_product/<int:product_id>", methods=["GET", "POST"])
def delete_product(product_id):
    cnx = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DB_NAME
    )
    cnx.autocommit = True
    cursor = cnx.cursor()

    sql = '''
        DELETE FROM product WHERE id = {} RETURNING *;
    '''.format(product_id)
    cursor.execute(sql)

    deleted_rows = cursor.fetchall()

    cursor.close()
    cnx.close()

    if deleted_rows:
        return 'Produkt o id {} został usunięty'.format(product_id)
    else:
        return 'Nie znaleziono produktu o takim id!'


if __name__ == "__main__":
    app.run(debug=True)