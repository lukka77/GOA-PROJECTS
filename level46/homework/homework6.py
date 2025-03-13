# 6) Create a list comprehension that generates a list of numbers from 1 to 50 that are divisible by 3.

divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(divisible_by_3)