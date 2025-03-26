def repeat_characters(word, n):    
    for char in word:
        for _ in range(n):
            yield char


rc = repeat_characters("abc", 3)

print(next(rc))  # 'a'
print(next(rc))  # 'a'
print(next(rc))  # 'a'
print(next(rc))  # 'b'
print(next(rc))  # 'b'
print(next(rc))  # 'b'
print(next(rc))  # 'c'
print(next(rc))  # 'c'
print(next(rc))  # 'c'