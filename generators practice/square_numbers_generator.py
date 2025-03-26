def square(n):
    i = 1
    while i <= n:
        yield i**2
        i += 1

sqr = square(5)

print(next(sqr))
print(next(sqr))
print(next(sqr))
print(next(sqr))
print(next(sqr))
