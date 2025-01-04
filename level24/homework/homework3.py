# 3) slicing და indexing დავალებები:

# Get the first element from a list.
list=[10, 20, 30, 40, 50]
first_element=list[0]
print(first_element)

# Get the last element from a list using negative indexing.
last_element=list[-1]
print(last_element) 

# Slice the first three elements of a list.
first_three_elements=list[:3]
print(first_three_elements)



# Extract the last five elements from a string.
string="GOA, academy!"
last_five_chars=string[-5:]
print(last_five_chars)

# Reverse a string using slicing.
reversed_string=string[::-1]
print(reversed_string)



# Get every third element from a list - ყოველი მესამე ელემენტი სიიდან
list=[10, 20, 30, 40, 50, 60, 70, 80, 90]
every_third_element=list[::3]
print(every_third_element)