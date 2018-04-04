from psycopg2 import connect, ProgrammingError
from flask import Flask, request

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'baza_db'

app = Flask(__name__)


def execute_sql(sql):
    cnx = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DB_NAME
    )
    cnx.autocommit = True
    cursor = cnx.cursor()

    cursor.execute(sql)
    try:
        result = cursor.fetchall()
    except ProgrammingError:
        result = None

    cursor.close()
    cnx.close()
    return result


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == 'GET':    ##name: nazwę produktu,
#description: opis produktu,
#price: cenę produktu.
        return '''
        <html>
            <body>
                <form method='post' action='#'>
                    <label>Nazwa produktu: </label><input type='text' name='name' /><br>
                    <label>Opis produktu: </label><input type='text' name ='description' /><br>
                    <label>Cena produktu: </label><input type='text' name = 'price'/><br>
                </form>
            </body> 
        </html>
        '''
    elif request.method == 'POST':
        form = request.form
        execute_sql('''
            INSERT INTO items VALUES (DEFAULT, '{}', '{}', {});
        '''.format(form['name'], form['description'], form['price']))

        return 'Dodano produkt'

    else:
        return 'Błędne dane'



if __name__ == "__main__":
    app.run(debug=True)

