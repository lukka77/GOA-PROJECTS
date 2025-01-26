# 2) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.

def welcome_message(name, age):
    return f"Hello, {name}! You are {age} years old. Welcome!"

name = "Luka"
age = 15
print(welcome_message(name, age))
