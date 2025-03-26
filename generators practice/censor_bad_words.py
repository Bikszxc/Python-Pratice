def censor_bad_words(sentence, censored):
    for word in sentence.split():
        clean_word = word.strip("!,.").lower()
        if clean_word in censored:
            yield "****" + word[len(clean_word):]
        else:
            yield word

censor = censor_bad_words("This is a bad movie, very ugly!", ["bad", "ugly"])

print(next(censor))  # "This"
print(next(censor))  # "is"
print(next(censor))  # "a"
print(next(censor))  # "****"  (bad is censored)
print(next(censor))  # "movie,"
print(next(censor))  # "very"
print(next(censor))  # "****"  (ugly is censored)