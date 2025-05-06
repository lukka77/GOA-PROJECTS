# 2) Lambda function that adds 5 to a given number
add_five = lambda x: x + 5
print("Add 5 to 10:", add_five(10))  # Output: 15

# 3) Lambda function to multiply two numbers
multiply = lambda a, b: a * b
print("Multiply 4 and 5:", multiply(4, 5))  # Output: 20

# 4) Lambda function to check if a number is even
is_even = lambda n: n % 2 == 0
print("Is 6 even?", is_even(6))  # Output: True

# 5) Lambda to convert Celsius to Fahrenheit
celsius_list = [0, 20, 30, 100]
fahrenheit_list = list(map(lambda c: (c * 9/5) + 32, celsius_list))
print("Temperatures in Fahrenheit:", fahrenheit_list)

# 6) Lambda to check if a string starts with 'A'
starts_with_a = lambda s: s.startswith('A')
print("Does 'Apple' start with 'A'?", starts_with_a("Apple"))  # Output: True

# 7) Add 10 to every number in a list
numbers = [1, 2, 3, 4, 5]
add_10 = list(map(lambda x: x + 10, numbers))
print("Add 10:", add_10)

# 8) Convert a list of strings to uppercase
words = ["hello", "world", "car"]
upper_words = list(map(str.upper, words))
print("Uppercase:", upper_words)

# 9) Find the length of each word in a list
lengths = list(map(len, words))
print("Lengths:", lengths)

# 10) Square each number in a list
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# 11) Convert a list of integers to strings
str_numbers = list(map(str, numbers))
print("As strings:", str_numbers)

# 12) Concatenate "Hello " to each name in a list
names = ["Luka", "Buba", "Gio"]
greetings = list(map(lambda name: "Hello " + name, names))
print("Greetings:", greetings)

# 13) Subtract 5 from every element in a list
subtracted = list(map(lambda x: x - 5, numbers))
print("Subtract 5:", subtracted)

# 14) Multiply each number in a list by 3
tripled = list(map(lambda x: x * 3, numbers))
print("Tripled:", tripled)

# 15) Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

# 16) Check if numbers in a list are greater than 50
check_gt_50 = list(map(lambda x: x > 50, [10, 60, 45, 80]))
print("Greater than 50:", check_gt_50)

# 17) Keep only even numbers
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even_nums)

# 18) Select numbers greater than 10
nums2 = [5, 12, 7, 20, 3, 15]
greater_than_10 = list(filter(lambda x: x > 10, nums2))
print("Numbers > 10:", greater_than_10)

# 19) Keep strings longer than 5 characters
words = ["apple", "banana", "orange", "car"]
long_words = list(filter(lambda w: len(w) > 5, words))
print("Strings > 5 characters:", long_words)

# 20) Remove empty strings
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda s: s != "", strings))
print("Non-empty strings:", non_empty)

# 21) Select only positive numbers
nums3 = [-5, 3, -1, 8, 0, -2, 10]
positive_nums = list(filter(lambda x: x > 0, nums3))
print("Positive numbers:", positive_nums)

# 22) Keep names starting with 'A'
names = ["Toma", "Bob", "Andria", "Beqa", "Ana"]
a_names = list(filter(lambda name: name.startswith("A"), names))
print("Names starting with 'A':", a_names)

# 23) Get numbers divisible by 3
nums4 = [3, 5, 9, 12, 14, 18]
div_by_3 = list(filter(lambda x: x % 3 == 0, nums4))
print("Divisible by 3:", div_by_3)

# 24) Keep words containing the letter 'e'
words2 = ["sun", "tree", "sky", "leaf", "moon"]
with_e = list(filter(lambda w: 'e' in w, words2))
print("Words with 'e':", with_e)

# 25) Remove None values
mixed_list = [1, None, 2, None, 3, 4]
no_none = list(filter(lambda x: x is not None, mixed_list))
print("Without None:", no_none)

# 26) Keep numbers ≤ 50
nums5 = [25, 60, 45, 90, 50, 10]
lte_50 = list(filter(lambda x: x <= 50, nums5))
print("Numbers ≤ 50:", lte_50)
