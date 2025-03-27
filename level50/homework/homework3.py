# 3)Try adding an integer to a string and catch the TypeError

try:
    result = "Hello" + 5
    print(result)
except TypeError:
    print("Error: Cannot concatenate a string and an integer.")
