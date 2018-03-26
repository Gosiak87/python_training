class Product:
    next_id = 1     # atrybut klasy Product
    def __init__(self, name, description, price, quantity):   # w inicie wpisujemy atrybuty obiektu ktory bedzie sie wyonywal na tym konstruktorze
        if not isinstance(description, str):     # jesli nie jest opis stingiem
            self.description = "underfined"
        if not isinstance(name, str):     # jesli nie jest nazwa stingiem
            self.name = "underfined"

        if (not isinstance(price, float)) or price < 0.01:
           price = 0.01

        if (not isinstance(quantity, int)) or quantity <= 0:
            quantity = 1

        self.name = name
        self.price = price
        self.quantity = quantity

        self._id = Product.next_id
        Product.next_id += 1       # Product.next_id czyli odwolanie do atrybutu next_id klasy Product


    def get_total_sum(self):
        if self.quantity >= 3:
            return self.price * self.quantity * 0.8
        result = self.price * self.quantity
        return result

    def get_id(self):
        return self._id


class ShoppingCart:
    def __init__(self):
        self.products = {}                  # pusty slownik

    def add_product(self, new_product):                           # domyslnie wyszikuwanie nastepuje po kluczach nie po wartosciach
        self.products[new_product.get_id()]= new_product      # dodaj sie do slowanika : nawiasy kwadrowt  ["klucz"] = wartosc w tym przypadku ne product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]


    def change_product_quantity(self, product_id, new_quantity):
        if product_id in self.products:
            product = self.products[product_id]
            product.quantity = new quantity
           # self.products[product_id].quantity = new_quantity  # wyciagamy ze slownika  product id

    def print_receipt(self):
        total_sum = 0
        for product in self.products.values(): # drukowanie produktów
            print("{} - {}, {}, {}".format(product.name, product.price, product.quantity,product.get_total_sum()))
            total_sum += product.get_total_sum()
            print ("Łączna kwota", total_sum)




banan = Product("Banan", "czikita", 1.00, 1)
cart = ShoppingCart()
cart.add_product(banan)
cart.change_product_quantity(banan.get_id(), 15)
cart.print_receipt()

a = Product("Samochod", "dla dzieci", 12, 4)
b = Product("Lalka", "dla dzieci", 15, 6)


print(a.get_id())
wynik = b.get_id()
print(wynik)
print(a.get_total_sum())
print(b.get_total_sum())



print("Zabawka:{},kosztował {}".format(a.get_id(), a.get_total_sum()))



