# 6) Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.

def insert_word(sentence, word, index):
    word = sentence.split()
    word.insert(index, word)
    return ''.join(word)

sentence = "Hello, Welcome!"
word="car"
index= 2
print(insert_word(sentence, word, index))