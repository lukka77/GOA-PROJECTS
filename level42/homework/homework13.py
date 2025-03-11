# Write a function that returns the sum of all numeric values in a dictionary.

dict2 = {
    "name": "Luka",
    "surname": "Gorgadze",
    "num": 34,
    "num2": 55,
    "num3": 11
}

sum_numbers = 0
for key, value in dict2.items():
    if type(value) == int or type(value) == float: sum_numbers += value
print(sum_numbers)