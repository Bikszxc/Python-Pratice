def vowel_counter(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for word in sentence.split():
        count = 0
        clean_word = word.strip("!,.").lower()
        for char in clean_word:
            if char in vowels:
                count += 1
        yield count

vc = vowel_counter("Hello world this is Python")

print(next(vc))  # 2  (Hello → e, o)
print(next(vc))  # 1  (world → o)
print(next(vc))  # 1  (this → i)
print(next(vc))  # 1  (is → i)
print(next(vc))  # 1  (Python → o)