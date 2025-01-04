# 4) შექმენით სია, რომელშიც იქნება 10 ელემენტი. მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი, num1 და num2. 
# თუ num1 მეტია num2-ზე, slicing მოახდინეთ სიაზე num1 ინდექსიდან num2 ინდექსამდე და დაბეჭდეთ ახალი სია.
#  თუ num2 მეტია num1-ზე, slicing მოახდინეთ სიაზე num2 ინდექსიდან num1 ინდექსამდე და დაბეჭდეთ ახალი სია.
#  თუ ეს ორი რიცხვი ტოლია, დაბეჭდეთ ცარიელი სია.


list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(list[num2:num1]) 

elif num2 > num1:
    print(list[num1:num2])

else:
    print([])
