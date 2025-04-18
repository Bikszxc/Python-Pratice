def fibonacci_sequence():
    x, y = 0, 1

    while True:
        yield x
        x, y = y, x + y

test = fibonacci_sequence()

for _ in range(20):
    print(next(test))