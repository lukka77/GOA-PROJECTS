# 11) Create a list comprehension that generates a sequence of Fibonacci numbers up to the 20th term.

fib_sequence = [0, 1] + [sum(fib_sequence[-2:]) for _ in range(2, 20)]
print(fib_sequence)