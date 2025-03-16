vowels = {'a', 'e', 'i', 'o', 'u'}

word = input("Enter a word: ")
transformed_word = ""

if len(word) <= 3:
    transformed_word = word
elif word[0].lower() in vowels:
    transformed_word = word + "way"
else:
    transformed_word = word[1:] + word[0] + "ay"

print(transformed_word)