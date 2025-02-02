# 8) Find the Maximum
# Create a function that takes a list of numbers and uses a loop to find and return the maximum number.

def find_the_maximum(numbers):
    max_numbers=numbers[0]
    for num in numbers:
        if num > max_numbers:
          max_numbers=num

    return max_numbers

result=find_the_maximum({ 1, 6, 2, 7, 9, 3, 11, 77})
print("The Maximum number is:", result)