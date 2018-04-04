# ex_1

print("Mam na imię Gosia")

# ex_2

a = input("Wpisz swoje imię: ")
b = input("Wpisz swoje nazwisko: ")
print(a + " " + b + " jest programistą Pythona!")

# ex_3

a = 2   # przechowuje typ danych int
b = 2.5  #przechowuje typ danych float
c = 'Python'  #przechowuje danych string
d = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.''' # przechowuje typ danych wielolinijkowy napis
e = True  #przechowuje typ danych bool

# ex_4

print('Zmienna a typu int')
print('Zmienna b typu float')
print('Zmienna c typu string')
print('Zmienna d typu wielolinijkowy napis')
print('Zmienna e typu bool')

# ex_5

a = 10
b = 20
x = a == b
print(x)

# Zwrócony wynik to false. Znak == przyrównuje zmienną a do zmiennej b.


# ex_6

add1 = 12
add2 = 3.5
sum = add1 + add2
print(add1, type(add1))
print(add2, type(add2))
print(sum, type(sum))

# ex_7

a1 = 10
a2 = 15
sum_ = a1 + a2
quotus = a2/a1
int_part = int(quotus)
print(a1)
print(a2)
print(sum_)
print(quotus)
print(int_part)

# ex_8

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[6])

# ex_9

my_array = ["Harry", "Ron", "Hermione"]
print(my_array[0])
print(my_array[2])

# ex_10

alphabet = ['a', 'b', 'c', 'd', 'e']
print(*alphabet)


# ex_11

a = 4
b = 7
resultModulo = a % b
print(resultModulo)

# ex_12

counter = 145
print(counter)
counter = counter + 1
print(counter)
counter = counter - 1
print(counter)

# ex_13

a = 6
b = 9
result = 6 > 9
print(result)

# ex_14

father = 1974
child = 2007
difference = child - father
new_str = str(difference)
print('Ojciec jest starszy od dziecka o ' + new_str + ' lat.')

# ex_15

result = 11 / 7
new_str = str(result)
print('11 : 7 = ' + new_str)

# ex_16

name = input('Podaj swoje imię: ')
year = int(input('Podaj rok swojego urodzenia: '))
now = 2018
age = now - year
new_str = str(age)
print(name + ": " + new_str)










