# 6) Write a function that takes a sentence and returns a list of words.

def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return ' '.join(words)

sentence = "Hello, Welcome!"
word = "car"
index = 2
print(insert_word(sentence, word, index))
