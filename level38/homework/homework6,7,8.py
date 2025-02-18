# 6) Set Creation & Basic Operations: Create a set with at least five elements, add a new element, remove an existing one, and check if a specific value is present in the set.

# 7) Set Union & Intersection: Create two sets with some common elements and perform union, intersection, and difference operations.

# 8) Removing Duplicates: Convert a list with duplicate elements into a set to remove duplicates and then convert it back to a list.



#6
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(2)

is_present = 3 in my_set

print("Updated set:", my_set)
print("Is 3 present in the set?", is_present)


#7
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union_result = set_a | set_b

intersection_result = set_a & set_b

difference_result = set_a - set_b

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference (set_a - set_b):", difference_result)


#8
my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
my_set = set(my_list)
unique_list = list(my_set)

print("Original list:", my_list)
print("List after removing duplicates:", unique_list)