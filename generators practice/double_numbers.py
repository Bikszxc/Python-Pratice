def double_numbers(numbers):
    for num in numbers:
        yield num*2

dn = double_numbers([2, 5, 8])

print(next(dn))  # 4  (2 * 2)
print(next(dn))  # 10 (5 * 2)
print(next(dn))  # 16 (8 * 2)