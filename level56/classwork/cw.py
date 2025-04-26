# Codewars

# 1) Expressions Matter
def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)

# 2) I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"

# 3) Reverse List Order
def reverse_list(l):
    return l [::-1]

# 4) Count Odd Numbers below n
def odd_count(n):
    return n//2

# 5) Difference of Volumes of Cuboids
def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    
    if v_a > v_b: return v_a - v_b
    return v_b - v_a

# 6) Drink about
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
# 7) Sort and Star
def two_sort(array):
    array.sort()
    
    res = ""
    for i in array[0]:
        res += i+"***"
    
    return res[:-3]

# 8) Grasshopper - Messi Goals
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# 9) Short Long Short
def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
    
# 10) My head is at the wrong end!
def fix_the_meerkat(arr):
    arr.reverse()
    return arr
