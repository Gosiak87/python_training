list_ = []
x = int(input('Podaj ilosc liczb : '))
for i in range(x):
    number = float(input('podaj liczby: '))
    list_.append(number)

sum_ = 0
for i in list_:
    sum_ = sum_ + i
avarage = sum(list_)/x

if sum_ > avarage:
    print('Suma:', sum_, 'średnia:', avarage, 'Suma jest większa!')
elif sum_ < avarage:
    print('Suma:', sum_, 'średnia:', avarage, 'Średnia jest większa!')
else:
    print('Suma:', sum_, 'średnia:', avarage, 'Suma równa średniej!')
