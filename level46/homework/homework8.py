# 8) Create a list comprehension that converts a list of temperature values in Celsius to Fahrenheit.

celsius = [0, 10, 20, 30, 40, 50, 60]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)