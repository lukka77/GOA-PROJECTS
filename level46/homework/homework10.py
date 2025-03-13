# 10) Create a list comprehension that extracts all words from a given sentence that contain at least one vowel and are longer than 5 characters.

sentence = "Hello, my name is Luka."
vowels = "aedas"
words = sentence.split()

filtered_words = [word for word in words if len(word) > 5 and any(vowel in word.lower() for vowel in vowels)]
print(filtered_words)