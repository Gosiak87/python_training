n = int(input('Podaj liczbę n :'))
list_ = []
for i in range(n+1):
    list_.append(i)

sum_ = 0
for i in list_:
    sum_ = sum_ + i

print(sum_)
