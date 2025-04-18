numbers = []

while True:
    try:
        user_input = int(input("Enter a number ('0' to end): "))
        
        if user_input == 0:
            break
        
        numbers.append(user_input)
    except ValueError:
        print("Invalid Input!")

if len(numbers) > 0:
    sum = 0
    for num in iter(numbers):
        sum += num
    print("List of all numbers:", numbers)
    print("Total:", sum)
else:
    print("No given numbers.")