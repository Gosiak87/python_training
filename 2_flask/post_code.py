from flask import Flask
from flask import request


app = Flask(__name__)   # przypisujemy aplikacje do zmiennej app

html = """
<html>
    <body>
        <form method="POST">
            <label> Wpisz kod pocztowy: <input name='code'></label>
            <br>
            <button type='submit'>Wyślij</button>
        </form>
    </body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def my_guess():
    if request.method == 'GET':
        return html

    elif request.method == 'POST':
        code = request.form['code']
        code_1 = code.split('-')

    try:
        for i in code_1:
                i = int(i)

    except ValueError :
            return 'Kod niepoprawny'
        if len(code_1) == 2 and len(code_1[0]) == 2 and len(code_1[1]) == 3:

            return 'Kod poprawny'

        else:
            return 'Kod niepoprawny'


if __name__ == '__main__':
    app.run(debug=True)