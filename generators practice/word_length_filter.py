def filter_animals(lst):
    for anim in lst:
        if len(anim) > 5:
            yield anim

animals = filter_animals(["dog", "elephant", "cat", "giraffe", "tiger"])
print(next(animals))  # "elephant"
print(next(animals))  # "giraffe"