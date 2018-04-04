from psycopg2 import connect, ProgrammingError
from flask import Flask, request

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'cinemas_db'

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


@app.route("/add_cinema", methods=["GET", "POST"])
def add_cinema():
    if request.method == 'GET':
        return '''
        <html>
            <body>
                <form method='post' action='#'>
                    <label>Nazwa: </label><input type='text' name='name' /><br>
                    <label>Adres: </label><input type='text' name='address' /><br>
                    <button type='submit'>Dodaj kino!</button>
                </form>
            </body> 
        </html>
        '''
    elif request.method == 'POST':
        form = request.form

        execute_sql('''
            INSERT INTO cinema VALUES (DEFAULT, '{}', '{}');
        '''.format(form['name'], form['address']))

        return '''
        <html>
            <body>
                <p>Dodano nowe kino!</p>
                <a href='/cinemas'>wróć</a>
            </body>
        </html>
        '''


@app.route("/cinemas", methods=["GET", "POST"])
def cinemas():
    if request.method == 'GET':
        cinemas_list = execute_sql('''
            SELECT * FROM cinema;
        ''')
    else:
        cinemas_list = execute_sql('''
            SELECT * FROM cinema WHERE name ILIKE '%{}%';
        '''.format(request.form['name']))

    cinemas_html = ''
    for row in cinemas_list:
        cinemas_html += '''
            <ul>
                <li>id: {0}</li>
                <li>name: {1}</li>
                <li>address: {2}</li>
                <li><a href='/del_cinema/{0}'>usuń</a></li>
            </ul>
        '''.format(*row)

    return '''
        <html>
            <body>
                <form method='post' action='#'>
                    <label>Nazwa: </label><input type='text' name='name' /><br>
                    <button type='submit'>Wyszukaj!</button>
                </form>
                <a href='/add_cinema'>dodaj kino!</a><br>
                {}
            </body>
        </html>
    '''.format(cinemas_html)


@app.route("/del_cinema/<int:cinema_id>", methods=["GET", "POST"])
def del_cinema(cinema_id):
    deleted_rows = execute_sql('''
        DELETE FROM cinema WHERE id = {} RETURNING *;
    '''.format(cinema_id))

    if deleted_rows:
        msg = 'Usunięto kino!'
    else:
        msg = 'Nie można usunąć kina bo go nie ma!'

    return '''
        <html>
            <body>
                <p>{}</p>
                <a href='/cinemas'>wróć</a>
            </body>
        </html>
    '''.format(msg)


if __name__ == "__main__":
    app.run(debug=True)