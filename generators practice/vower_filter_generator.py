def vowel_filter(sentence):
    vowels = {"a", "e", "i", "o", "u"}

    for char in sentence.lower():
        if char in vowels:
            yield char

vf = vowel_filter("hello world")

print(next(vf))
print(next(vf))
print(next(vf))