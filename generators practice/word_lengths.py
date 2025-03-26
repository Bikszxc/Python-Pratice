def word_lengths(sentence):
    for word in sentence.split():
        yield len(word.strip("!,."))

wl = word_lengths("Python is awesome!")

print(next(wl))  # 6  ("Python")
print(next(wl))  # 2  ("is")
print(next(wl))  # 7  ("awesome!")