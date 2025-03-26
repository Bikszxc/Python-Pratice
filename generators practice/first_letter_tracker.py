def first_letter_tracker(sentence):
    letters = set()
    for word in sentence.split():
        first_letter = word[0].upper()
        if first_letter not in letters:
            yield first_letter
            letters.add(first_letter)
        continue

tracker = first_letter_tracker("Hello world, hi again!")

print(next(tracker))  # "H"  (from "Hello")
print(next(tracker))  # "W"  (from "world")
print(next(tracker))  # "A"  (from "again") → "hi" skipped kasi may "H" na