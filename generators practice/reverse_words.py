def reverse_words(sentence):
    for word in sentence.split():
        yield word[::-1] 

rw = reverse_words("Python is fun")

print(next(rw))  # "nohtyP"
print(next(rw))  # "si"
print(next(rw))  # "nuf"