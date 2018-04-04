from psycopg2 import connect, ProgrammingError
from psycopg2.extras import RealDictCursor
from flask import Flask, request
import datetime

app = Flask(__name__)


USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'cinemas_db'


def execute_sql(sql):
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DB_NAME)
    cnx.autocommit = True
    cursor = cnx.cursor(cursor_factory=RealDictCursor)

    cursor.execute(sql)
    try:
        result = cursor.fetchall()
    except ProgrammingError:
        result = None

    cursor.close()
    cnx.close()
    return result


@app.route("/buy_ticket", methods=['GET', 'POST'])
def buy_ticket():
    if request.method == 'GET':
        return '''
        <html>
            <body>
                <p>Kup bilet:</p>
                <form method='post' action='#'>
                    <label>Cena: 15 PLN za szt.</label><br>
                    <label>Ile: </label><br>
                    <input type='number' name='quantity' min='1' /><br>
                    <button type='submit'>ZAREZERWUJ</button>
                </form>
            </body>
        </html>
        '''

    rows = execute_sql('''
        INSERT INTO tickets (quantity, price) VALUES ({}, 15.0) RETURNING *;
    '''.format(int(request.form['quantity'])))

    ticket_id = rows[0]['id']
    return '''
    <html>
        <body>
            Zarezerwowano, aby przejść do płatności kliknij <a href='/payment/{}'>TUTAJ</a>
        </body>
    </html>
    '''.format(ticket_id)


@app.route("/payment/<int:ticket_id>", methods=['GET', 'POST'])
def pay(ticket_id):
    if request.method == 'GET':
        return '''
        <html>
            <body>
                <p>Wybierz sposób płatności: </p>
                <form method='post' action='#'>
                    <select name='type'>
                        <option value='card'>Karta</option>
                        <option value='transfer'>Przelew</option>
                        <option value='cash'>Gotówka</option>
                    </select>
                    <button type='submit'>KUP</button>
                </form>
            </body>
        </html>
        '''


    execute_sql('''
        INSERT INTO payments VALUES ({}, '{}', '{}');        
    '''.format(ticket_id, request.form['type'], datetime.date.today()))

    return '''
    <html>
        <body>
            Kupiono, aby przejść do listy biletów kliknij <a href='/tickets'>TUTAJ</a>
        </body>
    </html>
    '''


@app.route("/tickets")
def tickets():
    # robimy tutaj LEFT JOIN zamiast JOIN ponieważ chcemy dostać wszystkie bilety,
    # a nie tylko te, dla których istnieje płatność (wtedy użylibyśmy JOIN)
    rows = execute_sql('''SELECT * FROM tickets LEFT JOIN payments ON tickets.id = payments.id;''')

    inner_html = ''
    for row in rows:
        if not row['type']:
            row['type'] = 'not paid'

        inner_html += '''
        <ul>
            <li>id: {}</li>
            <li>quantity: {}</li>
            <li>price: {}</li>
            <li>type: {}</li>
        </ul>
        '''.format(row['id'], row['quantity'], row['price'], row['type'])

    return '''
    <html>
        <body>
            {}
        </body>
    </html>
    '''.format(inner_html)


if __name__ == "__main__":
    app.run(debug=True)