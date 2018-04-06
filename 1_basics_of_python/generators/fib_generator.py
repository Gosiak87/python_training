def fib_generator(n):
    a, b = 0, 1

    for _ in range(n):
        yield(b)
        new_a = b
        new_b = a + b
        a = new_a
        b = new_b
        # a, b = b, a + b


for element in fib_generator(5):
    print(element)

