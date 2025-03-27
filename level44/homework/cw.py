# 1
def reverse_seq(n):
    res = []

    for i in range(n, 0, -1):
        res.append(i)

    return res

def reverse_seq(n):
    return list(range(n, 0, -1))

# 2
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"

    if p1 == "scissors":
        if p2 == "paper": return "Player 1 won!"
        else: return "Player 2 won!"
    elif p1 == "paper":
        if p2 == "scissors": return "Player 2 won!"
        else: return "Player 1 won!"
    else:
        if p2 == "paper": return "Player 2 won!"
        else: return "Player 1 won!"

# 3
def is_divisible(n,x,y):
    return n%x == 0 and n%y == 0

# 4
def count_sheep(n):
    if n == 0: return ""

    res = ""
    for i in range(1, n+1):
        res += f"{i} sheep..."

    return res

# 5
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3

    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    return "F"