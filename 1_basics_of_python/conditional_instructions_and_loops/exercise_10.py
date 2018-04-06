n = int(input('Wybierz liczbę z przedziału 1-10: '))

table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for i in table:
    result = (n*i)
    print(i, ' * ', n, ' = ', result)
    i += 1
