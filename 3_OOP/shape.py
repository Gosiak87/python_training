import math

class Shape:
    def __init__(self, _x, _y, _color):
        if not type(_x) == int:  # jesli typ x nie jest liczba to: (moze tez byc: if type(x) != int and type(x)!= float
            # moze tez byc komenda isinstance sprawdza czy to co jest pierwszym argumentem  jest intem lub floatem, ale potrzebujemy sprawdzic czy nie jest wiec piszemy
            # if not isinstance(x, (int, float)):
            _x = 0               # pod x = 0
        self._x = _x  # w ciele inita musimy sie odwolac do argumentach w naglowku

        if not type(_y) == int:  # jesli  typ y nie jest liczba to:
            _y = 0
        self._y = _y  # odwolujemy sie do argumentu naglowku

        if not type(_color) == str:
            _color = "Black"
        self._color = _color

    def print_info(self):    # metoda wypisujaca info
        # mozna tez tak: print("x: {}, y: {}, color: {}".format(self._x, self._y, self._color))
        print(self)
        print(self._x)
        print(self._y)
        print(self._color)

    def get_distance(self, other_shape):
        return math.sqrt((self._x - other_shape._x) ** 2 + (self._y - other_shape._y)** 2)


class Circle(Shape):        # klasa Circle, dziedziczy po klasie shape. Sprawdzamy co ma kalsa bazowa kopiujemy je i dodajemy nowe argumenty.
    def __init__(self, x, y, color, radius):
        super(Circle, self).__init__(x, y, color)      # dziedziczy te argumenty od klasy bazowej
        if (not isinstance(radius,(int, float))) or radius < 0:
            radius = 0
        self.radius = radius

    def print_info(self):
        super(Circle, self).print_info()  # dziedziczy po klasie bazowej
        print(" radius: {}".format(self.radius))   # chronione( z jednym podkreslnikiem) atrybuty musisz mozesz w klasie dziedziczacej,

    def area(self):   # pole powierzchni
        return math.pi * (self.radius ** 2)

    def circuit(self):  # obwód
        return 2 * math.pi * (self.radius)


shp = Shape(5, "placek", 50)
shp.print_info()

shp1 = Shape(2, 2, "black")

shp1.print_info()
print("odleglosc wynosi: {:2f}".format(shp.get_distance(shp1)))


circlel = Circle(3, 4, "black", 6)
circlel.print_info()

print("Pole: ", circlel.area())
print ("Obwod: ", circlel.circuit())