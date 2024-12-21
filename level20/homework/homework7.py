# 7) Write a program that checks if a single given number is prime number

num1 = int(input("Enter your number: "))
is_valid = True

if num1 < 0:
     is_valid = False


for i in range(2, num1):


     if num1 % i == 0:
         is_valid = False

if is_valid == True: print("Your number is prime")
else: print("Your number is not prime")