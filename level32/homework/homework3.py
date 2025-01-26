# 4) Write a function that takes a first name and last name, capitalizes them, and formats them into a single string.

def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

first_name = "Luka"
last_name = "Gorgadze"
print(format_name(first_name, last_name))
