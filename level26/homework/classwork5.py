# 5) Find Maximum: Create a function that takes a list of numbers and returns the maximum value.

def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

numbers = [3, 4, 7, 2, 8, 5]
print(find_maximum(numbers))