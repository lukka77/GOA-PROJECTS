# 2)Create a list and try to access an index that does not exist. Handle IndexError.

my_list = [10, 20, 30, 40, 50]

try:
    index = 10
    print(f"The value at index {index} is: {my_list[index]}")
except IndexError:
    print(f"Error: The index {index} is out of range. Please enter a valid index.")