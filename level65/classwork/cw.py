# საკლასო დავალება:
# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = 'aeiou'
    return sum(1 for char in sentence if char in vowels)