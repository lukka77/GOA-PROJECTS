# 2) Tuple Indexing & Slicing: Create a tuple with at least 5 elements and extract the second, last, and a slice of the middle three elements.

# 3) Tuple Immutability: Try to modify an element in a tuple and observe what happens.

# 4) Tuple Packing & Unpacking: Create a tuple with multiple values, unpack them into separate variables, and print each variable.

# 5) Tuple Methods: Use the .count() and .index() methods on a tuple containing repeated elements to count occurrences and find the first occurrence of a specific value.




#2
my_tuple = (10, 20, 30, 40, 50)
second_element = my_tuple[1]
last_element = my_tuple[-1]
middle_slice = my_tuple[1:4]

print("Second element: ", second_element)
print("Last element: ", last_element)
print("Middle three elements: ", middle_slice)

#  5
tuple3 = (1, 2, 3, 4, 5, 1, 1, 1)
print(tuple3.count(1))
print(tuple3.index(2))

#4
my_tuple = (1, "GOA", 7.77)
a, b, c = my_tuple

print(a)
print(b)
print(c)