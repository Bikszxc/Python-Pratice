height = int(input("Enter a number: "))

for i in range(1, height + 1):
    print(" " * (height - i), end='')
    for num in range(1, i+1):
        print(num, end='') 

    for num in range(i - 1, 0, -1):
        print(num, end='')

    print()