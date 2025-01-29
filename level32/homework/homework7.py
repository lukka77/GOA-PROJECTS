# 7) Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.

def sentence_to_words(sentence):
    return sentence.split() 

sentence = "Hello, Welcome!"
print(sentence_to_words(sentence))