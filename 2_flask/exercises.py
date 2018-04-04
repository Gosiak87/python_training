from datetime import datetime

from flask import Flask, request   # zaimportowaliscmy flaska do naszej aplikacji

app = Flask(__name__)   #zapisujemy do zmiennej ze bedziemy modulu uzywac wplikacji, ze modul (__name_ bedzie aplikacja flaska i zapisujemy do zmiennej app)


@app.route("/hello_world")   #  dekorujemy zmienną metodą route(metodą drogowskazu, która wskazuje droge-strone). Pod tym adresem ma byc wynik tej funkcji .
def hello():                 # funkcją okresla jak ma dzialac aplikacja
    return "Hello World"


@app.route("/dzis")
def today():
    return str(datetime.now())


@app.route("/greet/<name>")   # w nawiasach <> jak definiujemy to zawsze bedzie string
def greet(name):
    return "Hello" + name


#@app.route("/age/<int:yo>")
#def age(yo):
#    return "Next year you will by {} y.o".format(yo)


@app.route("/age/<int:yo>")
def age(yo):
    return "Next year you will by {} y.o".format(yo + 1)

html = """ <html>
<body>
    <form method="POST">
        <label>Imię: <input name="first_name"></label>
        <br>
        <label>Nazwisko: <input name="last_name"></label>
        <br>
        <button type="submit">Wyślij</button>
    </form>
</body>
</html>"""

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":  # jesli odpowiedz
        return html
    else:
        return "Czesc {} {}!".format(
                request.form["first_name"],
                request.form["last_name"])




if __name__== "__main__":
    app.run(debug=True)      # tak ruszamy aplikacje bo tak sobie wymyslili tworcy flaska
