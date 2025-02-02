# 7) Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional statements. Print "Even" for even numbers and "Odd" for odd numbers.

def check_even_odd(num):
    for num in num:
        if num %2 ==0:
            print(f"{num} -- even")
        else:
            print(f"{num} -- odd")

check_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9])