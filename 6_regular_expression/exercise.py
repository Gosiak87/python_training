import re

text_to_search = open('text.txt').read()

result = re.findall(r'autor', text_to_search, re.I)     # parametr re.I mowi o tym zeby pokazac wszystko niezaleznie od wielkosci liter. Znajdź wszystkie wystąpienia wyrazu autor.
print(result)

result = re.findall(r'\W(autor)\W', text_to_search)     # wypisuje sam wyraz autor (a nie wyraz autor czescia slow np. autrorytarny),Jesli wyraz jest w nawiasach witedy bedzie nam sie pokazywal bez znakow bialych np spacji
print(result)
 # \w = [a-zA-Z]+
 # print(re.findall(r'\[a-zA-Z] {2,}\.', text_to_search))  tutaj {2} oznacza ze ilosc wyrazów ma byc od dwoch

result = re.findall(r'\d%', text_to_search)         # Znajdź wszystkie wystąpienia pasujące do wzoru <ciąg_cyfr>%.
print(result)

result = re.findall(r'\w+\.', text_to_search)      # Znajdź wszystkie wystąpienia wyrazów, które kończą się znakiem ..
print(result)

result = re.findall(r'\w*polski\w*', text_to_search, re.IGNORECASE)  # Znajdź wszystkie wyrazy, w których znajduje się ciąg znaków polski (niezależnie od wielkości znaków
print(result)  # \w*polski\w* gwiazdka przed i po mowi ze kazy wyraz prze i kazdy wyraz po