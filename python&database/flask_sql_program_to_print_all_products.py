from psycopg2 import connect
from flask import Flask, request

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DB_NAME = 'exercise_db'

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    cnx = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=DB_NAME
    )
    cnx.autocommit = True
    cursor = cnx.cursor()

    html = """
    <html>
        <body>
            <p>Lista produktów:</p>
            {}
        </body>
    </html>
    """

    sql = """
        SELECT * FROM product;

    """
    cursor.execute(sql)

    inner_html = ''
    for row in cursor:
        inner_html += """
        <ul>
            <li>id: {}</li>
            <li>name: {}</li>
            <li>description: {}</li>
            <li>price:{}

        </ul >""".format(*row)  # (*row) = (row[0], row[1], row[2], row[3])

    cursor.close()
    cnx.close()
    return '''
    <html>
        <body>
            <p>Lista produktów:</p>
            {}
        </body>
    </html>
    '''.format(inner_html)


if __name__ == "__main__":
    app.run(debug=True)
