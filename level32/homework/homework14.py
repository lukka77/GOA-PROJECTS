# 14) Create a function that inserts an item at the end of a list using the insert method.

def insert_at_end(my_list, item):
    my_list.insert(len(my_list), item)

my_list = [1, 2, 3]
insert_at_end(my_list, 4)
print(my_list)
