def palindromes(sentence):
    for word in sentence.split():
        backward = word[::-1]
        if word.strip("!,.") == backward.strip("!,."):
            yield word

pal = palindromes("madam, racecar! python. level hello")
print(next(pal))  # "madam"
print(next(pal))  # "racecar"
print(next(pal))  # "level"