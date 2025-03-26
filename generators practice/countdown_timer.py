def countdown_timer(start, end, step):
    for i in range(start, end - 1, -step):
        yield i

cd = countdown_timer(10, 0, 2)

print(next(cd))  # 10
print(next(cd))  # 8
print(next(cd))  # 6
print(next(cd))  # 4
print(next(cd))  # 2
print(next(cd))  # 0