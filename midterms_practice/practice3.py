sqrd = []

def square_numbers(n):
    for i in range(1, n + 1):
        i = i ** 2
        sqrd.append(i)
        
    for i, item in enumerate(iter(sqrd), start=1):
        yield f"{i} ^ 2 = {item}"

while True:
    try:
        user_input = int(input("Enter the range: "))
        break
    except ValueError:
        print("Not a valid number.")

test = square_numbers(user_input)
    
for num in test:
    print(num)