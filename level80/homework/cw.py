# 2-6) შეასრულეთ ამოცანები:

# https://www.codewars.com/kata/57f609022f4d534f05000024
# Find the stray number
def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003
def solution(nums):
    if nums is None or nums == []: return []
    return sorted(nums)
# https://www.codewars.com/kata/583f158ea20cfcbeb400000a
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b
# https://www.codewars.com/kata/534ea96ebb17181947000ada
def break_chocolate(n, m):
    if n <= 0 or m <= 0: return 0
    return n*m-1
# https://www.codewars.com/kata/529eef7a9194e0cbc1000255
def is_anagram(test, original):
    def count_chars(s):
        res = {}
        # {"a": 1}

        for i in s:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1

        return res

    return count_chars(test.lower()) == count_chars(original.lower())