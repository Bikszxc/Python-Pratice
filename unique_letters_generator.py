def unique_letters(word):
    unique = set()
    for char in word.lower().strip(" "):
        if char not in unique:
            yield char
            unique.add(char)

ul = unique_letters("banana")

print(next(ul))  # 'b'
print(next(ul))  # 'a'
print(next(ul))  # 'n'