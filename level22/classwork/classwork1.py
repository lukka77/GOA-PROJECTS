# საკლასო დავალება: შექმენით სია, რომელშიც იქნება 10 ელემენტი. 
# შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ მთელი რიცხვის სახით.
# თუ ეს რიცხვი მეტია ან ტოლია 0-ზე და ნაკლებია სიის სიგრძეზე, მაშინ სიიდან ამ ინდექსზე მყოფი ელემენტი წამოიღეთ და დაბეჭდეთ.
# თუ ეს რიცხვი მეტია ან ტოლია "სიის სიგრძე გამრავლებული -1ზე" და ნაკლებია ან ტოლია -1 ზე, მაშინ დაბეჭდეთ ამ ინდექსზე მყოფი ელემენტი

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

user_number = int(input("Enter the number: "))

if user_number >= 0 and user_number < 10:
    print(list1[user_number])
elif user_number >= -10 and user_number <= -1:
    print(list1[user_number])
else:
    print("Wrong index")