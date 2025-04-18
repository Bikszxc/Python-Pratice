def multiples_of(num, n):
    for i in range(1, n + 1):
        yield f"{num} * {i} = {num * i}"

multiplication = multiples_of(9, 10)

for num in multiplication:
    print(num)