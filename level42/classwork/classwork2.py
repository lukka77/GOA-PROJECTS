# Create a Python program that initializes a dictionary with at least five key-value pairs. Perform the following operations:

# Print all the keys in the dictionary using the keys() method.
dict2 = {
    "name": "Luka",
    "surname": "Gorgadze",
    "age": 15,
    "city": "Batumi",
    "academy": "GOA"
}

for i in dict2:
    print(dict2[i])


# Print all the values in the dictionary using the values() method.
dict3 = {
    "name": "Luka",
    "surname": "Gorgadze",
    "age": 15,
    "city": "Batumi",
    "academy": "GOA"
}

print(dict3.values())


# Print all key-value pairs using the items() method.
dict4 = {
    "name": "Luka",
    "surname": "Gorgadze",
    "age": 15,
    "city": "Batumi",
    "academy": "GOA"
}

print(dict4.keys())


# Iterate over the dictionary using the items() method and print each key with its corresponding value in a formatted string.
dict5 = {
    "name": "Luka",
    "surname": "Gorgadze",
    "age": 15,
    "city": "Batumi",
    "academy": "GOA"
}

for key, value in dict5.items():
    print(key)
    print(value)