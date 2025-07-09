# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
def row_sum_odd_numbers(n):
    start_num = 1
    row = 1
    
    res = []
    
    for i in range(1, n+1):
        ls = []
        for x in range(i):
            ls.append(start_num)
            start_num += 2
        res.append(sum(ls))
        
    return res[-1]

# https://www.codewars.com/kata/56541980fa08ab47a0000040
def printer_error(s):
    valid = "abcdefghijklm"
    res = 0
    
    for i in s:
        if i not in valid: res +=1
        
    return f"{res}/{len(s)}"

# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(text):
    str_list=text.split(" ")
    result = []
    for i in str_list:
        result.append(i[::-1])
    return " ".join(result)

# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
def binary_array_to_number(arr):
    res = ""
    for bit in arr:
        res += str(bit)
    return int(res, 2)

# საკლასო დავალება:
# შეასრულეთ ამოცანა: https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    people = 0
    for i in bus_stops:
        people += i[0]
        people -= i[1]
    return people


# საკლასო დავალება:
# შეასრულეთ ამოცანა:
# https://www.codewars.com/kata/5949481f86420f59480000e7
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

# საკლასო დავალება:
# შეასრულეთ ამოცანა:
# https://www.codewars.com/kata/559590633066759614000063
def min_max(lst):
  return [min(lst), max(lst)]

