while True:                                    # dopoki prawda
    try:
        number1 = int(input("Wpisz liczbe 1: "))     # wszystko co jest przyjmowane z klawiatury jest stringiem
       # _number1 = int(number1)                # konwertuje na intigera
        number2 = int(input("Wpisz liczbe 2: "))
       # _number2 = int(number2)
        result = number1 / number2             # dzielenie
        print(result)
        break
    except ValueError:                         # spodziewaj sie bledu wartosci
        print("To nie jest liczba! Spróbuj ponownie.")        # jak bedzie zrob to
    except ZeroDivisionError:                  # spodziewaj sie bledu dzielenia przez zero
        print("Nie dziel przez zero")          # jak bedzie zrob to
