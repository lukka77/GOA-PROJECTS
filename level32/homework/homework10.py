# 10) Create a function that takes a list and a list of items, and appends each item to the original list.

def append_multiple_to_list(my_list, items):
    my_list.extend(items)

my_list = [1, 2, 3]
items_to_add = [4, 5, 6]
append_multiple_to_list(my_list, items_to_add)
print(my_list)
