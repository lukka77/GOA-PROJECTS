# Create a list comprehension that generates a list of all palindromic numbers between 10 and 200 
# (a palindromic number reads the same forward and backward).

list2 = [num for num in range (10, 200) if str(num) == str(num)[::-1]]
print(list2)