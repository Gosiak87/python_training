import hashlib


def hash_password(password):
    min_passw_lenght = 7
    if len(password) >= min_passw_lenght:
        special_charakter = '!@#$%^&*()_+-={}[]|\:";<>?,./"'
        numbers = '0123456789'
        for char in password:
            if char in special_charakter:
                special_charakter = True
        if special_charakter:
            return hashlib.md5(password.encode()).hexdiges


    # if any(password):
    #     return hashlib.md5(password.encode()).hexdigest
