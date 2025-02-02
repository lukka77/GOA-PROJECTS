# 10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.

def sum_divisible_by_three():
    total_sum=0
    for num in range(1, 100):
        if num % 3 == 0:
            total_sum +=num
    return total_sum
result= sum_divisible_by_three()
print("The sum of numbers divisable by 3 is:", result)