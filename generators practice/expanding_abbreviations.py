def expand_abbreviations(sentence, abbv):
    for word in sentence.split():
        clean_word = word.strip("!,.").lower()
        if clean_word in abbv:
            yield abbv.get(clean_word)
        else:
            yield word

expander = expand_abbreviations("IDK if I'll be there asap", {
    "idk": "I don't know",
    "asap": "as soon as possible"
})

print(next(expander))  # "I don't know"
print(next(expander))  # "if"
print(next(expander))  # "I'll"
print(next(expander))  # "be"
print(next(expander))  # "there"
print(next(expander))  # "as soon as possible"