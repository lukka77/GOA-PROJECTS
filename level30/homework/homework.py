# 2) Convert a given sentence to uppercase and print the result.

sentence = "hello"
uppercase_sentence=sentence.upper()
print(uppercase_sentence)

# 3) Take a user's name input and display it in uppercase letters.

name = input("Enter your name: ")
print(name.upper())


# 4) Create a function that converts a list of lowercase strings to uppercase

def convert_to_uppercase(str):
    return [string.upper() for string in str]
lowercase_strings=["hello", "goa"]
uppercase_strings=convert_to_uppercase(lowercase_strings)
print(uppercase_strings)


# 5) Convert all the characters of a given sentence to lowercase and print it.

sentence="HellO"
lowercase_sentence=sentence.lower()
print(lowercase_sentence)

# 6) Ask the user for their email address and ensure it is stored in lowercase.

email = input("Enter your email address: ")
email_lowercase = email.lower()
print("Your email in lowercase is:", email_lowercase)


# 7) Write a function that takes a mixed-case string and returns it in all lowercase letters.

def to_lowercase(mixed_case_string):
    return mixed_case_string.lower()

mixed_case_string="HelLo GoA"
lowercase_string=to_lowercase(mixed_case_string)
print(lowercase_string)

# 8) Capitalize the first letter of a sentence provided by the user.

sentence=input("Enter a sentence: ")
capitalized_sentence = sentence.capitalize()
print("Capitalized sentence:", capitalized_sentence)

# 9) Given a list of lowercase strings, capitalize the first letter of each string.

def capitalize_first_letter(strings):
    return [string.capitalize() for string in strings]

lowercase_strings = ["apple", "banana", "orange"]
capitalized_strings = capitalize_first_letter(lowercase_strings)
print(capitalized_strings)

# 10) Create a function that takes a string and returns it with the first letter capitalized

def capitalize_first_letter(string):
    return string.capitalize()

input_string = "hello"
capitalized_string = capitalize_first_letter(input_string)
print(capitalized_string)


# 11) Find the position of the first occurrence of the word "Python" in a sentence.

def find_python_position(sentence):
    position = sentence.find("Python")
    return position

sentence="Python"
position=find_python_position(sentence)
print("The position of the first occurrence of 'Python' is:", position)