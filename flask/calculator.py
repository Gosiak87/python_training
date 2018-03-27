#Napisz i uruchom prosty kalulator, który:

#* wyświetli formatkę z dwoma polami na wprowadzenie liczb i listę wybieraną operacji (+, -, *, /)
#* po wciśnięciu guzika "wyślij" policzy wynik i wyświetli go na ekranie


import Flask
from flask import request

app = Flask(__name__)

html = """ <html>
<body>
    <form method="POST">
        <label>l1<input type="number" name="l1"></label>
        <select name="operation">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        <br>
        <label>l2<input type="number" name="l2"></label>
        <br>
        <button type="submit">Wykonaj dzialanie</button>
    </form>
</body>
</html>"""


@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "GET":  #dane ktore wpisuje uzywtnik siedza w request.form w l1 i l2
        return html


if __name__== "__main__":
    app.run(debug=True)
