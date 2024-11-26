# 3) საკლასო დავალება:
# რიცხვის გამოცნობის პროგრამა:
# შექმენით my_num ცვლადი და 1-დან 10-მდე ნებისმიერი რიცხვი მიანიჭეთ მნიშვნელობად.
# სანამ მომხმარებლის შემოტანილი რიცხვი არ იქნება my_num-ის ტოლი, ისევ შეეკითხეთ მომხმარებელს ეს რიცხვი.
# საბოლოოდ დაუბეჭდეთ "you guessed" და რამდენი ცდა დაჭირდა

my_num = 7
user_num = int(input("Enter number: "))
counter = 0

while user_num != my_num:
    user_num = int(input("Enter number: "))
    counter += 1

print("you guessed")
print("Your guess count:", str(counter))
