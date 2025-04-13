# საკლასო დავალება:
# Write a function apply_to_list(func, values) that takes a function func and a list values, and returns a new list where func is applied to each element.
# Then:
# Define a function square(x) that returns the square of a number.

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def apply_to_list(func, values):
    return[func(value) for value in values]

def square(x):
    return x*x

result = apply_to_list(square, values)
print(result)