# 6) Factorial: Implement a function to calculate the factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6))
