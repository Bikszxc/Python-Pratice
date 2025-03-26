def reverse_sentence(sentence):
    sentences = [word for word in sentence.split()]
    for i in range(len(sentences) - 1, -1, -1):
        yield sentences[i]

rs = reverse_sentence("I love Python")
        
print(next(rs))  # "Python"
print(next(rs))  # "love"
print(next(rs))  # "I"