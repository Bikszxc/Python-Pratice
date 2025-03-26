def firstlast(words):
    for word in words:
        clean_word = word.strip("!.,").lower()
        if clean_word[0] == clean_word[-1]:
            yield word

inpt = firstlast(["level!", "civic...", "apple, rawr", "banana", "wow"])

try:
    while True:
        print(next(inpt))
except StopIteration:
    print("Tama na pareh!")