sentence = input("Enter a sentence: ").split()

words = {}

for word in sentence:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for word in sorted(words):
    print(f"{word}: {words[word]}")