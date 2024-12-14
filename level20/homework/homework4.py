# 4) Write a program that takes a score (0-100) as input and outputs the grade based on the following rules:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

score = int(input("Enter the score (0-100): "))

if 90 <= score <= 100:
    print("Grade: A")

elif 80 <= score < 90:
    print("Grade: B")

elif 70 <= score < 80:
    print("Grade: C")

elif 60 <= score < 70:
    print("Grade: D")

else:
    print("Grade: F")