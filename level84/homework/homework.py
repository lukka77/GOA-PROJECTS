# 2-6)
# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b
def reverse_letter(st):
    filtered_st = ""
    
    for i in st:
        if i.isalpha():
            filtered_st += i
    return filtered_st[::-1]

# https://www.codewars.com/kata/545a4c5a61aa4c6916000755
def gimme(input_array):
    sorted_arr = sorted(input_array)
    mid_l = sorted_arr [1]
    
    return input_array.index(mid_l)

# https://www.codewars.com/kata/5a03b3f6a1c9040084001765
def angle(n):
    return (n-2)*180

# https://www.codewars.com/kata/55d1d6d5955ec6365400006d
def round_to_next5(n):
    if n%5 == 0: return n
    
    return (n//5 + 1) * 5

# https://www.codewars.com/kata/511f11d355fe575d2c000001
def two_oldest_ages(ages):
    ages = sorted(ages)
    
    return [ages[-2], ages[-1]]