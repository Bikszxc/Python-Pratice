digits = int(input("Enter a number: "))
converted = str(digits)

print(converted)

numbers = []

for num in converted:
    add = int(num)
    numbers.append(add)

print("Sum of digits:", sum(numbers))
