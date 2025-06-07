# codewars

# 1  https://www.codewars.com/kata/52fba66badcd10859f00097e
def disemvowel(string):
    vowels = "aeiouAEIOU"
    res = ""

    for i in string:
        if i not in vowels:
            res += i

    return res

# 2  https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    return int("".join([str(int(d)**2) for d in str(num)]))
def square_digits(num):
    st = []

    for i in str(num):
        int_i = int(i)
        sq_i = int_i**2
        st.append(str(sq_i))

    return int("".join(st))


# 3 https://www.codewars.com/kata/554b4ac871d6813a03000035
def high_and_low(numbers):
    nums = list(map(int, numbers.split(" ")))
    return f"{max(nums)} {min(nums)}"


# 4 საკლასო დავალება:
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    return [item for item in l if isinstance(item, int)]



# 5



# 6



# 7