# 3) Create a list of all even numbers between 1 and 20 using list comprehension.

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)