# 7) Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.

for i in range(5):
    i= int(input("Enter a number: "))
    print("even" if i % 2 == 0 else "odd")