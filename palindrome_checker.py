phrase = input("Enter a word or phrase: ")
backward = phrase[::-1]

palindrome = True

if backward != phrase:
    palindrome = False

if palindrome:
    print("This is a palindrome")
else:
    print("Not a palindrome")