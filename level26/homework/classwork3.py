# 3) Even or Odd: Create a function that determines whether a given integer is even or odd.

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(4))
print(is_even_or_odd(7))