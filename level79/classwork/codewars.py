# https://www.codewars.com/kata/555eded1ad94b00403000071
def series_sum(n):
    if n==0:
        return "0.00"
    if n==1:
        return "1.00"

    res = 1
    divisor = 4
    for i in range(n-1):
        res += 1/divisor
        divisor += 3

    final = str(round(res, 2))
    if len(final.split(".")[1])==1:
        return final + "0"
    return final

# https://www.codewars.com/kata/544aed4c4a30184e960010f4
def divisors(integer):
    divisors = []

    for i in range(2, integer):
        if integer%i==0:
            divisors.append(i)

    if len(divisors) == 0:
        return f"{integer} is prime"
    return divisors

# https://www.codewars.com/kata/563cf89eb4747c5fb100001b
def remove_smallest(numbers):
    if numbers == []:
        return []
    lst = numbers
    minimal = lst.index(min(numbers))
    return lst[:minimal] + lst[minimal+1:]

# საკლასო დავალება:

# შეასრულეთ ამოცანა:
# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
def number(lines):
    result = []
    for i in range(len(lines)):
        result.append(str(i + 1) + ": " + lines[i])
    return result
