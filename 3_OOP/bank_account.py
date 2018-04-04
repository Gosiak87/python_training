
class BankAccount:
    def __init__(self, number):
        self._number = number
        self._cash = 0.0

    def get_number(self):
        return self._number

    def get_cash(self):
        return self._cash

    def deposit_cash(self, amount):   # zwiekszenie wartości atrybutu cash o podaną watość.
        if type(amount) != int and amount < 0:  # jesli typ amount jest rozny od liczby i amount jest mniejsze od 0
            amount = 0

        self._cash += amount

    def withdraw_cash(self, amount):  # zmniejszenie wartosci atrybutu cash
        if type(amount) != int or amount < 0:  # musi byc or, bo wtedy skupia sie na pierwszym warunku
            amount = 0

        if amount > self._cash:
            amount = self._cash

        self._cash -= amount
        return amount

    def print_info(self):
        print("Numer konta: {}, Stan konta: {}".format(self._number, self._cash))    # ma wyświetlić informację o numerze konta i jego stanie.


ba = BankAccount(12345)
ba.deposit_cash(1000)
print("wypłacono {} zlotych".format(ba.withdraw_cash("pincet")))
ba.print_info()
ba.withdraw_cash(-20)
ba.withdraw_cash(600)
ba.print_info()
