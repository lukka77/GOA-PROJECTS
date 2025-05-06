# 2-5)
# https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89
def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"


# https://www.codewars.com/kata/5933a1f8552bc2750a0000ed
def nth_even(n):
    return 2 * (n - 1)


# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
def replace_exclamation(st):
    return ''.join('!' if char in 'aeiouAEIOU' else char for char in st)


# https://www.codewars.com/kata/59441520102eaa25260000bf
def unusual_five():
    return len("hello")


# https://www.codewars.com/kata/559d2284b5bb6799e9000047
def add_length(s):
    return [f"{word} {len(word)}" for word in s.split()]