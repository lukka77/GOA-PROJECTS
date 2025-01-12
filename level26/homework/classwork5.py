# 5) Find Maximum: Create a function that takes a list of numbers and returns the maximum value.

def find_max(num_list):
    max_value =num_list[0]

    for num in num_list:
        if num > max_value:
            max_value=num

    print(max_value)

find_max([1, 4, 2, 3, 10, 3, 5])