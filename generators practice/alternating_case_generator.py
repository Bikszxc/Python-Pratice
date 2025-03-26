def alternate_case(word):
    for i, char in enumerate(word.replace(" ", "")):
        yield char.upper() if i % 2 == 0 else char.lower() 

ac = alternate_case("python is sigma")

try:
    while True:
        print(next(ac), end="")
except StopIteration:
    print("\nDone!")


