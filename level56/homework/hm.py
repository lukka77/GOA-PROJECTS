# 2) Print your name
print("Luka Gorgadze")

# 3) Print a favorite quote
print('"The best Academy -- GOA ."')

# 4) Print multiple lines
print("Roses are white")
print("Violets are blue")
print("Coding is fun")

# 5) Print a simple math result
print(2 + 3)

# 6) Print a shape with symbols
print("  *  ")
print(" *** ")
print("*****")

# 7) Convert string to integer
num_str = "42"
num_int = int(num_str)
print(num_int)

# 8) Add two floats
a = 3.5
b = 2.5
print(a + b)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 10) Print data types
x = 10          
y = "hello"     
z = 7.2        
print(type(x))
print(type(y))
print(type(z))

# 11) User input and type conversion
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# 12) Ask for your name
name = input("What is your name? ")
print("Hello, " + name + "!")

# 13) Ask for age and calculate next year’s age
age = int(input("How old are you? "))
print("Next year, you will be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:", num1 + num2)

# 15) Favorite color
color = input("What is your favorite color? ")
print("Your favorite color is " + color + "!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough!")
else:
    print("You need to grow a bit more!")

# 17) Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
text = "Python"
for letter in text:
    print(letter)


# 19) Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum from 1 to 10:", total)

# 20) Multiplication table for 2 (1 to 5)
for i in range(1, 6):
    print("2 x", i, "=", 2 * i)

# 21) Print even numbers between 2 and 20
for i in range(2, 21, 2):
    print(i)

# 22) Print numbers from 1 to 5 using while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5 using while loop
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum from 1 to 5:", total)

# 24) Count down from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print odd numbers between 1 and 10
i = 1
while i <= 10:
    if i % 2 == 1:
        print(i)
    i += 1

# 26) Ask for input until "exit"
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

# 27) Print all elements of a list
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# 28) Find length of a list
my_list = [5, 10, 15, 20]
print("The list has", len(my_list), "elements.")

# 29) Access a specific element from the list
numbers = [10, 20, 30, 40]
print("Second element:", numbers[1])

# 30) Add an element to the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Updated list:", fruits)

# 31) Remove an element from the list
colors = ["red", "blue", "green"]
colors.remove("blue")
print("List after removal:", colors)

# 32) Create a list of squares
squares = [x ** 2 for x in range(1, 6)]
print("List of squares:", squares)

# 33) Create a list of even numbers
evens = [x for x in range(2, 11) if x % 2 == 0]
print("Even numbers:", evens)

# 34) Filter odd numbers from a list
nums = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in nums if x % 2 != 0]
print("Odd numbers:", odds)

# 35) Convert a list of strings to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)

# 36) List of numbers squared if divisible by 2
mixed_nums = [1, 2, 3, 4, 5, 6]
squared_evens = [x ** 2 for x in mixed_nums if x % 2 == 0]
print("Squared evens:", squared_evens)

# 37) Function to greet a user
def greet_user(name):
    print("Hello, " + name + "!")

greet_user("Alice")

# 38) Function to add two numbers
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(5, 7))

# 39) Function to check if a number is even or odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print("7 is", check_even_odd(7))
print("8 is", check_even_odd(8))

# 40) Function to calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width

print("Area:", area_rectangle(5, 3))

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reversed:", reverse_string("Python"))

# 42) Create and print a tuple
my_tuple = (42, "hello", 3.14)
print("Tuple:", my_tuple)

# 43) Access an element in a tuple
sample_tuple = ("apple", "banana", "cherry", "date")
print("Second element:", sample_tuple[1])

# 44) Find the length of a tuple
print("Length of tuple:", len(sample_tuple))


# 45) Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Concatenated tuple:", combined_tuple)

# 46) Check if an item exists in a tuple
my_tuple = ("apple", "banana", "cherry")
if "banana" in my_tuple:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {"red", "green", "blue"}
print("Set:", my_set)

# 48) Check if an element is in a set
colors = {"yellow", "pink", "orange"}
if "pink" in colors:
    print("Yes")
else:
    print("No")

# 49) Add an element to a set
colors.add("purple")
print("Updated set:", colors)

# 50) Remove an element from a set
colors.remove("yellow")
print("Set after removal:", colors)

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of sets:", union_set)

# 52) Create and print a dictionary
person = {"name": "Datha", "age": 25}
print("Dictionary:", person)