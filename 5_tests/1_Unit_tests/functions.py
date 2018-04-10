from datetime import datetime


def div(a, b):
    if not isinstance(a, (int, float)):
        return None
    if not isinstance(b, (int, float)):
        return None
    #if b is not int:
     #   return None
    if b == 0:
        return None

    return a / b


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    pesel_length = 11
    if(len(pesel)) != pesel_length:
        return None
    for digit in pesel[:-1]:
        try:
            digits_sum += int(digit) * weights[weight_index]
            weight_index += 1
        except ValueError:
            return None
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    if day > 31:
        return None
    if 0 < month <13 :
        birth_date = datetime(int("19" + pesel[0:2]), month, day)
    elif 20 < month <33:
        birth_date = datetime(int("20" + pesel[0:2]), month -20, day)
    try:
        last_number = int(pesel[-1])
    except ValueError:
        return None
    result = {
        "pesel": pesel,
        "valid": validate == last_number,
        "gender": gender,
        "birth_date": birth_date
    }
    return result


