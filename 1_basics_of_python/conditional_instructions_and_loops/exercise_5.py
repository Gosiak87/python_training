import math
print('Rownanie w postaci a*x**2 + b*x + c ==0')
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))
delta = b**2-4*a*c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)

    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('x_1 =', x1, 'x_2 =', x2)
else:
    print('Brak rozwiazan w zbiorze liczb rzeczywistych. ')
