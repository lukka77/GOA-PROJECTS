# Create a list comprehension that generates a list of all
# numbers between 1 and 100 that are divisible by either 3 or 5, but not both.

list2 = [x for x in range(1, 100) if (x %3 == 0) != (x %5 == 0)]
print(list2)