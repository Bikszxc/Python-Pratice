import random

def scramble_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    for word in words:
        yield word

scrambled = scramble_sentence("I love Python programming, miss ko na siya")

try:
    while True:
        print(next(scrambled))
except StopIteration:
    print("Done!")