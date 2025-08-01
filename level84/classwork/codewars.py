# https://www.codewars.com/kata/586f6741c66d18c22800010a
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number,end_number + 1,step))

# საკლასო დავალება:

# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))


# https://www.codewars.com/kata/539ee3b6757843632d00026b
def capitals(word):
    res = []

    for i in range(len(word)):
        char = word[i]

        if char.isupper(): res.append(i)

    return res

# https://www.codewars.com/kata/57cc981a58da9e302a000214
def small_enough(array, limit):
    for i in array:
        if i > limit: return False
    return True

# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError

    result = 1
    for i in range(2, n+1):
        result *= i

    return result

# http://codewars.com/kata/5813d19765d81c592200001a/train/python
def dont_give_me_five(start,end):
    res = 0 
    for i in range(start, end + 1):
        if "5" not in str(i):
            res+=1
        return res
    

# საკლასო დავალება:
# https://www.codewars.com/kata/526c7363236867513f0005ca
def is_leap_year(year):
    return (year % 100 and not year % 4) or not year % 400