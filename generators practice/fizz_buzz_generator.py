def fizzbuzz():
    i = 0
    while True:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i

rawr = fizzbuzz()

for _ in range(50):
    print(next(rawr))