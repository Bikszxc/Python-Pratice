def cycle_list(lst):
    while True:
        for item in lst:
            yield item

c = cycle_list(["A", "B", "C"])

print(next(c))  # A
print(next(c))  # B
print(next(c))  # C
print(next(c))  # A (repeats)
print(next(c))  # B
print(next(c))  # C