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


@app.route("/add_seance", methods=["GET", "POST"])
def add_seance():
    if request.method == 'GET':
        cinemas = execute_sql('''SELECT * FROM cinemas;''')
        cinemas_html = ''
        for cinema in cinemas:
            cinemas_html += '''<option value='{}'>{}</option>'''.format(cinema['id'], cinema['name'])

        movies = execute_sql('''SELECT * FROM movies;''')
        movies_html = ''
        for movie in movies:
            movies_html += '''<option value='{}'>{}</option>'''.format(movie['id'], movie['name'])

        return '''
        <html>
            <body>
                <p>Dodaj seans:</p>
                <form method='post' action='#'>
                    <label>Kino: </label><br>
                    <select name='cinema_id'>
                        {}
                    </select>
                    <br>
                    <label>Film: </label><br>
                    <select name='movie_id'>
                        {}
                    </select>
                    <br>
                    <button type='submit'>dodaj</button>
                </form>
            </body>
        </html>
        '''.format(cinemas_html, movies_html)
    else:
        form = request.form

        msg = 'Dodano seans'
        try:
            execute_sql('''
                INSERT INTO seances VALUES (DEFAULT, {}, {})
            '''.format(form['cinema_id'], form['movie_id']))
        except IntegrityError:
            msg = 'Taki seans już istnieje!'

        return '''
        <html>
            <body>
                <p>{}</p>
                <a href='/cinemas'>kina</a>
                <a href='/movies'>filmy</a>
            </body>
        </html>
        '''.format(msg)


@app.route("/cinemas", methods=["GET", "POST"])
def cinemas():
    # wyświetlanie kin, które mają w repertuarze wybrany film
    if request.method == 'GET':
        movies = execute_sql('''SELECT * FROM movies;''')
        movies_html = ''
        for movie in movies:
            movies_html += '''<option value='{}'>{}</option>'''.format(movie['id'], movie['name'])

        return '''
        <html>
            <body>
                <p>Wyszukaj kina, w których leci podany film:</p>
                <form method='post' action='#'>
                    <label>Film: </label><br>
                    <select name='movie_id'>
                        {}
                    </select>
                    <br>
                    <button type='submit'>wyszukaj</button>
                </form>
            </body>
        </html>
        '''.format(movies_html)
    else:  # POST
        form = request.form
        movies = execute_sql('''SELECT * FROM movies;''')
        movie_name = ''
        for movie in movies:
            if movie['id'] == int(form['movie_id']):
                movie_name = movie['name']
                break

        cinemas = execute_sql('''
            SELECT * FROM cinemas
            JOIN seances ON cinemas.id = seances.cinema_id WHERE movie_id = {};
        '''.format(form['movie_id']))
        cinemas_html = '<ul>'
        for cinema in cinemas:
            cinemas_html += '''<li>{}</li>'''.format(cinema['name'])
        cinemas_html += '<ul>'

        return '''
        <html>
            <body>
                <p>Wszystkie kina w których grają film {}:</p>
                {}
            </body>
        </html>
        '''.format(movie_name, cinemas_html)


@app.route("/movies", methods=["GET", "POST"])
def movies():
    # wyświetlanie filmów, które są wyświetlane w wybranym kinie
    if request.method == 'GET':
        cinemas = execute_sql('''SELECT * FROM cinemas;''')
        cinemas_html = ''
        for cinema in cinemas:
            cinemas_html += '''<option value='{}'>{}</option>'''.format(cinema['id'], cinema['name'])

        return '''
        <html>
            <body>
                <p>Wyszukaj kina, w których leci podany film:</p>
                <form method='post' action='#'>
                    <label>Film: </label><br>
                    <select name='cinema_id'>
                        {}
                    </select>
                    <br>
                    <button type='submit'>wyszukaj</button>
                </form>
            </body>
        </html>
        '''.format(cinemas_html)
    else:  # POST
        form = request.form
        cinemas = execute_sql('''SELECT * FROM cinemas;''')
        cinema_name = ''
        for cinema in cinemas:
            if cinema['id'] == int(form['cinema_id']):
                cinema_name = cinema['name']
                break

        movies = execute_sql('''
            SELECT * FROM movies
            JOIN seances ON movies.id = seances.movie_id WHERE cinema_id = {};
        '''.format(form['cinema_id']))
        movies_html = '<ul>'
        for movie in movies:
            movies_html += '''<li>{}</li>'''.format(movie['name'])
        movies_html += '<ul>'

        return '''
        <html>
            <body>
                <p>Wszystkie filmy, które grają w kinie {}:</p>
                {}
            </body>
        </html>
        '''.format(cinema_name, movies_html)


if __name__ == "__main__":
    app.run(debug=True)