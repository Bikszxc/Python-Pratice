def word_generator(sentence):
    for word in sentence.split():
        yield word

wg = word_generator("Hello world, how are you?")

print(next(wg))  # "Hello"
print(next(wg))  # "world,"
print(next(wg))  # "how"
print(next(wg))  # "are"
print(next(wg))  # "you?"