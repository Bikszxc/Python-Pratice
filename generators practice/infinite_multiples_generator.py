def multiples_of(n):
    num = n
    while True:
        yield num
        num += n

m = multiples_of(3)

print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))