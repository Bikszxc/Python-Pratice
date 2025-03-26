def ordinal_numbers():
    i = 0

    while True:
        i += 1
        last_two = i % 100
        last_digit = i % 10 

        if 10 <= last_two <= 13:
            yield str(i) + "th"
        elif last_digit == 1:
            yield str(i) + "st"
        elif last_digit == 2:
            yield str(i) + "nd"
        elif last_digit == 3:
            yield str(i) + "rd"
        else:
            yield str(i) + "th"

ord_gen = ordinal_numbers()

for _ in range(200):
    print(next(ord_gen))