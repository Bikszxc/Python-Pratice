message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))
starting_point = "a"

for char in message:
    shifted_char = chr((ord(char) - starting_point + shift) % 26 + starting_point)
    print(shifted_char, end='')