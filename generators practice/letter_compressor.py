def compress_letters(text):
   
    previous_char = text[0]
    count = 0
        
    for char in text:
        if char == previous_char:
            count += 1
        else:
            yield f"{previous_char}{count}"
            previous_char = char
            count = 1

    yield f"{previous_char}{count}"

compressed = compress_letters("aaabbcddddee")  
print(next(compressed))  # "a3"  
print(next(compressed))  # "b2"  
print(next(compressed))  # "c1"  
print(next(compressed))  # "d4"  
print(next(compressed))  # "e2"  