def double_letter_words(sentence):
    for word in sentence.split():
        previous_char = ''
        for char in word.strip("!.,"):
            if char == previous_char:
                yield word
                break
            previous_char = char

doubles = double_letter_words("I needed a good book for .. tomorrow.")
print(next(doubles))  # "need"
print(next(doubles))  # "good"
print(next(doubles))  # "book"
print(next(doubles))  # "tomorrow"