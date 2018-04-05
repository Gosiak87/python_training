# function_1


def square(num):
    return num ** 2


print("2 podniesione do potęgi drugiej, to:", square(2))  # powinno być 4
print("16^2=", square(16))  # powinno być 256
print("256 do potęgi 2 =", square(256))  # powinno być 65536

# function_2


def multiply(subcject, times):
    return subcject * times


print("100 * 100 =", multiply(100, 100))  # 10000
print("2 razy 2 to", multiply(2, 2))  # 4
print("15 * 10 =", multiply(15, 10))  # 150


# function_3

def power(base, exponent=2):
    return base ** exponent


print("2 do potęgi 6 to", power(2, 6))  # 64
print("4 do potęgi 8 to", power(4, 8))  # 65536


# function_4


def convert_to_usd(zlotys):
    return "{0:.2f}".format(zlotys / 3.85)


print("385PLN = ", convert_to_usd(385), "USD")
print("100PLN = ", convert_to_usd(100), "USD")


# function_5


def create_name(name, surname, nickname):
    return print(name + '"' + nickname + '"' + surname)


create_name("Jan", "Kowalski", "Siwy")


# function_6


def calculate_net(gross, vat):
    return gross / (1 + vat)


print(calculate_net(123, 0.23))
print(calculate_net(20, 0.08))


# function_7

def square_area(a, b):
    return a * b


print(square_area(7, 6))


# function_8

def circle_circuit(diameter):
    return diameter * 3.14

# 3.14
# obwod = srednica *liczba pi


print(circle_circuit(36))


# function_9

def dogs_age(age):       # przyjmuje za parametr wiek psa
    if age <= 2:        # jesli psa wiek to rowne lub mniejsze od 2
        return age * 10.5   # wiek * 2
    else:                # jesli nie zostal pierwszy warunek spelniony to wykonaj drugi warunek
        result = (2 * 10.5) + ((age - 2) * 4)  # dla pierwszych dwoch lat *10,5 + wiek -2 *4
        return result


print(dogs_age(5))
print(dogs_age(1.5))


# function_10

def chessboard(n=8):
    i = 0
    while i < n:    # funkcja sie bedzie powtarzac dopoki i bedzie 8
        if i%2 == 0:     # w przypadku kiedy reszta z mnozenia jest rowna 0 to sa parzyste
            print(' # # # #')
        else:
            print('# # # #')
        i += 1


chessboard(8)


# function_11

def find_number(num):
    if num % 4 == 0:
        return True
    else:
        return False


print(find_number(8))
print(find_number(9))

# function_12


def histogram(numbers):
    if all(isinstance(i, int) for i in numbers):   # jesli instancja wszystkich elementów jest typem int to dla kazego elementu...
        for i in numbers:
            print(i * "#")
    else:
        return None


histogram([2, 3, 4, 5])
histogram([1, 2, 'error!'])


# function_13

def create_list(arg1, arg2):
    return [arg1, arg2] * 4


print(create_list(1, 2))
print(create_list(True, False))

# function_14


def list_keys(d):
    return [key for key in d]
    #return list(d.keys())


my_dict = {
    "title": "A New Hope",
    "episode": "4",
    "feature": "Death Star"
}


print(list_keys(my_dict))

# function_15


def max_length(d):
    return [key for key in d if len(key) < 5]


print(max_length(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie']))


# function_16

def sum(numbers):
    result = 0
    for i in numbers:
        result += i
    return result


print(sum([2, 4, 5, 6]))


# function_17

def mean(numbers):
    return sum(numbers) / len(numbers)


print(mean([2, 3, 4]))


# function_18


def message(d):
    if "movie" in d and "name" in d and "role" in d:
        description = "In {}, {} is a {}.".format(d["movie"], d["name"], d["role"])
        return description
    else:
        return None


input_dict = {
    "movie": "Kevin sam w domu",
    "name": "Macaulay Culkin",
    "role": "Kevin",
}

print(message(input_dict))


# function_19

def make_tuple(a, b, c=3, d=4):
    return a, b, c, d


print(make_tuple('Michał', 'Gosia'))


# function_20

def find_first_and_last(*args):
    for i in args:
        result = args[0], args[-1]
    return result

     #return (i for i in args if args[0] or args[-1])


print(find_first_and_last('Zosia', 23, 'Basia', 13, 'b', 8))

# function_21


def find_boundaries(user_list):
    my_list = []
    only_numbers = []
    for element in user_list:
        if type(element) == int or type(element) == float:
            only_numbers.append(element)
        else:
            continue
    my_list.append(min(only_numbers))
    my_list.append(max(only_numbers))

    return my_list


print(find_boundaries(['zero', 2, 1.5, 'one', 100, 'two', 2]))
print(find_boundaries([1, 5, 2, 3.5, -1]))
print(find_boundaries([0, 2, "a kuku!", 10]))

# function_22


def censor(words):
    curses = ('Java', 'C#', 'Ruby', 'PHP')
    for i in curses:
        words = words.replace(i, '*' * len(i))   # replace ma dwa parametry(stary, nowy razy dlugosc slowa
    return words


print(censor("Java is the best, but PHP is the bestest!"))
print(censor("C# is the best, but Python is the bestest!"))
print(censor("Cobol is the best, but Ruby is the bestest!"))


# function_23

def check_palindrom(text):
    if text == text[::-1]:         # odwrocenie tekstu
        return True
    else:
        return False


print(check_palindrom("kajak"))
print(check_palindrom("niekajak"))


# function_24

def safe_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None


if __name__ == "__main__":

    print(safe_get(["Harry", "Ron", "Hermione"], 2))

# function_25


def divide(a, b):

    try:
        _a = int(a)
        _b = int(b)
    except ValueError:
        return None

    if a < 0 or b < 0:
        return None

    if _a != a or _b != b:
        return None

    try:
        return a / b
    except ZeroDivisionError:
        return None


if __name__ == "__main__":

    print(divide(1.0, 100))


# function_26

def phone(number):
    numbers = ["997", "998", "999"]
    if number in numbers:
        return True
    else:
        raise Exception("Nie ma takiego numeru !")


if __name__ == "__main__":

    print(phone("999"))

    print(phone("123"))




