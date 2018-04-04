

class Employee:
    def __init__(self, uid, first_name, last_name):
        self.id = uid
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):     # seter to jest metoda ktora ustala wartosc dla atrybutów prywatnych
        if isinstance(new_salary, (int, float)) and new_salary >= 0:
            self._salary = new_salary


class HourlyEmployee(Employee):
    def compute_payment(self, hours):
        return self._salary * hours     # hours to jest zmienna uzywana w fukcji





adam = Employee(1, "Adam", "Kowalski")
print("Zarabiasz {} PLN". format(adam.get_salary()))
adam.set_salary(7.50)
zosia = HourlyEmployee(2, "Zosia", "Nowak")
zosia.set_salary(6.30)
print("Zosia zarobia: {}".format(zosia.compute_payment(160)))

