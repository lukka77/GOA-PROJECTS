# 7) Create a list comprehension that extracts words with more than 4 letters from a given list of words.

words = ["car", "phone", "sport", "internet", "apple", "house"]
long_words = [word for word in words if len(word) > 4]
print(long_words)