def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

rs = running_sum([2, 5, 1, 7])

print(next(rs))  # 2
print(next(rs))  # 7  (2 + 5)
print(next(rs))  # 8  (2 + 5 + 1)
print(next(rs))  # 15 (2 + 5 + 1 + 7)