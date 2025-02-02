# 9) Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.

def positive_numbers(numbers):
    positive_numbers=[]
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
        return positive_numbers
result=positive_numbers([-3, -2, -1, 1, 2, 3])
print("Postive numbers:", result)