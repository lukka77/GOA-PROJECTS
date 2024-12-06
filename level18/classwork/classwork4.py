# საკლასო დავალება: 
# მომხმარებელს შემოატანინეთ 2 რიცხვი, num1, num2.
# თუ პირველი მეტია მეორეზე, შექმენით დიაპაზონი მეორე რიცხვიდან პირველი რიცხვის ჩათვლით და დაბეჭდეთ მხოლოდ ლუწი.
# ხოლო თუ მეორე რიცხვი მეტია პირველზე, შექმენით დიაპაზონი პირველიდან მეორეს ჩათვლით და დაბეჭდეთ მხოლოდ კენტი რიცხვები.
# საბოლოოდ დაბეჭდეთ ყველა ამ დაბეჭდილი რიცხვის ჯამი.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    even_numbers = (i for i in range(num2, num1+1) if i % 2 == 0)
    print("- even:", even_numbers)
    print("sum:", sum(even_numbers))

else:
    odd_numbers = (i for i in range(num1, num2+1) if i % 2 != 0)
    print("- odd:", odd_numbers)
    print("sum:", sum(odd_numbers))