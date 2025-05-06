# codewars

# 1) Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

# 2) Lario and Muigi Pipe Problem
def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))

# 3) Plural
def plural(n):
    return n == 0 or n > 1

# 4) Multiplication table for number
def multi_table(number):
    res = ""
    for i in range(1,11):
        res += f"{i} * {number} = {i*number}\n"
    return res[0:-1]

# 5) Super Duper Easy
def problem(a):
    if type(a) == str: return "Error"
    return a*50+6

# 6) Grasshopper - If/else syntax debug
def check_alive(health):
    if health > 0:
        return True
    else:
        return False
    
# 7) Grasshopper - Basic Function Fixer
def add_five(num):
    total = num + 5
    return total

# 8) Grasshopper - Terminal game combat function
def combat(health, damage):
    if health - damage > 0: return health - damage
    return 0

# 9) საკლასო დავალება:
# https://www.codewars.com/kata/595970246c9b8fa0a8000086
def capitalize_word(word):
    return word[0].upper() + word[1:]


# 10) How many lightsabers do you own?
def how_many_light_sabers_do_you_own(*args):
    if len(args) == 0: return 0
    return 18 if args[0] == "Zach" else 0

# 11) საკლასო დავალება:
# https://www.codewars.com/kata/563b74ddd19a3ad462000054
# Stringy Strings
def stringy(size):
    return ('10' * size)[:size]

# 12) Remove duplicates from list
def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result

# 13) საკლასო დავალება:
# https://www.codewars.com/kata/5899642f6e1b25935d000161
def merge_arrays(arr1, arr2):
    result = []
    for num in arr1 + arr2:
        if num not in result:
            result.append(num)
    return sorted(result)