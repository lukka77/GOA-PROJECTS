# CODEWARS

# https://www.codewars.com/kata/59cfc000aeb2844d16000075
def capitalize(s):
    even = [s[i].upper() if i % 2 == 0 else s[i] for i in range(len(s))  ]
    odd = [s[i].upper() if i % 2 != 0 else s[i] for i in range(len(s))  ]
    return ["".join(even),"".join(odd)]

# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
def no_odds(values):
    return [x for x in values if x%2 == 0]

# https://www.codewars.com/kata/5a3dd29055519e23ec000074
def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == "":
            score += 0
        elif arr2[i] == arr1[i]:
            score += 4
        else: score-= 1
    if score < 0:
        return 0
    return score

# საკლასო დავალება:
# https://www.codewars.com/kata/5b180e9fedaa564a7000009a
def solve(s):
    l = len([i for i in s if i.islower()])
    u = len(s) - l

    if l >= u: return s.lower()
    return s.upper()

# საკლასო დავალება:
# https://www.codewars.com/kata/58fa273ca6d84c158e000052
def digits(n):
    return len(str(n))