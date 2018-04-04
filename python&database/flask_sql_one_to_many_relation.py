from psycopg2 import connect, ProgrammingError, IntegrityError
from psycopg2.extras import RealDictCursor
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
    cursor = cnx.cursor(cursor_factory=RealDictCursor)

    cursor.execute(sql)
    try:
        result = cursor.fetchall()
    except ProgrammingError:
        result = None

    cursor.close()
    cnx.close()
    return result


@app.route("/buy_ticket", methods=["GET", "POST"])
def buy_ticket():
    if request.method == 'GET':
        seances = execute_sql('''
            SELECT * FROM seances;
        ''')
        seances_html = ''
        for seance in seances:
            seances_html += '''<option value='{}'>{}</option>'''.format(seance['id'], seance['name'])

        return '''
        <html>
            <body>
                <form method='post' action='#'>
                    <label>Cena za bilet: 12.00 PLN</label><br>
                    <label>Seans:</label>
                    <select name='seance_id'>
                    {}
                    </select>
                    <br>
                    <label>Liczba biletów: </label><br>
                    <input type='number' name='quantity' />
                    <button type='submit'>kup!</button>
                </form>
            </body>
        </html>
        '''.format(seances_html)
    else:  # POST
        form = request.form

        inserted_rows = execute_sql('''
            INSERT INTO tickets VALUES (DEFAULT, {}, 12.00, {}) RETURNING *;
        '''.format(form['quantity'], form['seance_id']))

        new_ticket_id = inserted_rows[0]['id']
        return '''
        <html>
            <body>
                <p>Kupiono bilet!</p>
                <a href='/ticket/{}'>szczegóły biletu</a>
            </body>
        </html>
        '''.format(new_ticket_id)


@app.route("/ticket/<int:ticket_id>", methods=["GET", "POST"])
def ticket(ticket_id):
    rows = execute_sql('''
        SELECT * FROM tickets JOIN seances ON tickets.seance_id=seances.id WHERE tickets.id = {};
    '''.format(ticket_id))

    ticket = rows[0]

    return '''
    <html>
        <body>
            <p>ID seansu: {}</p>
            <p>nazwa filmu: {}</p>
            <p>nazwa kina: {}</p>
            <p>liczba osób: {}</p>
            <p>cena za osobę: {}</p>
            <a href='/buy_ticket'>kup bilet</a>
        </body>
    </html>
    '''.format(ticket['id'], ticket['name'], ticket['cinema_name'], ticket['quantity'], ticket['price'])


if __name__ == "__main__":
    app.run(debug=True)