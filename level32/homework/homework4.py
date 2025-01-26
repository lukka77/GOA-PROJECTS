# 5) Create a function that takes a string, reverses it, and formats it within a sentence.

def reverse_and_format(sentence):
    reversed_sentence = sentence[::-1]
    return f"The reversed sentence is: {reversed_sentence}"

text="Hello, Welcome!"
print(reverse_and_format(text))