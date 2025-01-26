# 11) Create a function that appends all elements of one list to another list.

def append_all_elements(source_list, target_list):
    target_list.extend(source_list)

target_list = [1, 2, 3]
source_list = [4, 5, 6]
append_all_elements(source_list, target_list)
print(target_list)
