# 1) საკლასო დავალება: მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში მთელი რიცხვის სახით.
# შემდეგ შექმენით დიაპაზონი 0-დან ამ რიცხვამდე და დაბეჭდეთ დიაპაზონის ყველა რიცხვის ჯამი.
# გამოიყენეთ for ციკლი


num= int(input("Enter number: "))
sum = 0

for i in range( num ):
    sum = sum + i

print(sum)
