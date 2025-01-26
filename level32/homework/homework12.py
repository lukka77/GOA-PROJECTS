# 12) Write a function that takes a list, an index, and an item, and inserts the item at the specified index.

def insert_item_at_index(my_list, index, item):
    my_list.insert(index, item)

my_list = [1, 2, 3, 5]
insert_item_at_index(my_list, 3, 4)
print(my_list)