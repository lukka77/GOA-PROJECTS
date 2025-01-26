# 8) Write a function that takes a paragraph and splits it into sentences based on periods.

def split_into_sentences(paragraph):
    return [sentence.strip() for sentence in paragraph.split('.') if sentence]

paragraph = "This is the first sentence."
sentences = split_into_sentences(paragraph)
print(sentences)