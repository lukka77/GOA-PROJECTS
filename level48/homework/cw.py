# 2-6)
# შეასრულეთ ამოცანები:

# https://www.codewars.com/kata/56b1f01c247c01db92000076
# https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1
# https://www.codewars.com/kata/5aa736a455f906981800360d
# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
# https://www.codewars.com/kata/55cbc3586671f6aa070000fb

# 1
def double_char(s):
    return ''.join([char * 2 for char in s])

# 2
def get_age(age):
    return int(age[0])

# 3
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

# 4
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

# 5
def check_for_factor(base, factor):
    return base % factor == 0