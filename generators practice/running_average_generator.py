from statistics import mean

def running_average():
    numbers = []
    number = yield "GOGOGO!"

    while True:
        if number is None:
            break
        numbers.append(number)
        number = yield mean(numbers)

avg_gen = running_average()
print(next(avg_gen))  # Dapat may unang numero bago mag-next!
print(avg_gen.send(5))  # 5.0
print(avg_gen.send(10)) # 7.5  (average ng [5, 10])
print(avg_gen.send(15)) # 10.0 (average ng [5, 10, 15])