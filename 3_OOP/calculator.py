
class Calculator:        # definiujemy klase kalkulator
    def __init__(self):  # konstruktor - mowimy mu ze w kazdym stowrzonym obiekcie tej klasy (nowym kalkulatorze) ma byc pusta lista
        self.operations = []  # historia operacji w kalkulatorze

 # po  kolei metody w tej klasie
    def add(self, num1, num2): #   self jest zawsze plus inne parametry
        result = num1 + num2
        msg = "added {} to {}, got {}".format(num1, num2, result)  # metoda format do napisu
        self.operations.append(msg)  # dodajemy do listy historii msg
        return result

    def multiply(self, num1, num2): #   self jest zawsze
        result = num1 * num2
        msg = "multiplied {} to {}, got {}".format(num1, num2, result)  # metoda format do napisu
        self.operations.append(msg)  # dodajemy do listy historii msg
        return result

    def subtract(self, num1, num2):  # self jest zawsze
        result = num1 - num2
        msg = "subtracted {} to {}, got {}".format(num1, num2, result)  # metoda format do napisu
        self.operations.append(msg)  # dodajemy do listy historii msg
        return result

    def divide(self, num1, num2):  # self jest zawsze
        result = num1 / num2
        msg = "divided {} to {}, got {}".format(num1, num2, result)  # metoda format do napisu
        self.operations.append(msg)  # dodajemy do listy historii msg
        return result

    def print_operations(self):
        for operation in self.operations:  # dla kazdekj operacji w liscie naszych operacji
            print(operation)

    def clear_operations(self):
        self.operations.clear()   # czysci liste operacji


class AdvancedCalculator(Calculator):
    def pow(self, num1, num2):
        result = num1 ** num2
        msg = "{}^{} equels {}".format(num1, num2, result)
        self.operations.append(msg)
        return result

    def root(self, num1, num2):
        result = num1 ** (1/num2)
        msg = "root {} of {}  {}".format(num2, num1, result)   # w zadaniu napisane ze najpierw num2  a potem num1
        self.operations.append(msg)
        return result

    @staticmethod
    def compute_circle_area(radius):     # ta metoda nie moze zapisywac wyniku na liscie operacji. poniewaz jest wywolywana na klasie, a klasa nie ma atrybutu operations (nie ma dostepu do listy operacji, bi nie ma self, wiec nie ma sie do czego odwolac)
        return AdvancedCalculator.PI * (radius ** 2)


print(AdvancedCalculator.compute_circle_area(2))


calc = AdvancedCalculator()
print(calc.add(2, 2))
calc.clear_operations()
print(calc.add(5, 3))
calc.multiply(3, 5)
calc.subtract(0, 25)
calc.divide(19, 2)
calc.pow(2, 4)
calc.root(27, 3)
calc.print_operations()


