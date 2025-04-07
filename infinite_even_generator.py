# Problem: Infinite Alternating Case Generator
# Write a generator function called alternating_case(text) that yields 
# each letter of a string, alternating between uppercase and lowercase forever.

# gen = alternating_case("hello")
# for _ in range(10):
#    print(next(gen), end="")

# Expected output:
# HeLlOhElLo


def alternating_case(text):
    toggle = True

    while True:
        for i, char in enumerate(text):
            yield char.upper() if toggle else char.lower()
            toggle = not toggle
            

gen = alternating_case("angelyn")

for _ in range(50):
    print(next(gen), end="")

