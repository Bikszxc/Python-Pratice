import re

def count_unique_letters(sentence):
    for word in sentence.split():
        clean_word = re.sub(r'\W', '', word).lower()
        yield len(set(clean_word)) 

unique_counter = count_unique_letters("hello world good day!")
print(next(unique_counter))  # 4  (hello → h, e, l, o)
print(next(unique_counter))  # 5  (world → w, o, r, l, d)
print(next(unique_counter))  # 3  (good → g, o, d)
print(next(unique_counter))  # 3  (day → d, a, y)