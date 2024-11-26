# 2) საკლასო დავალება: 
# შექმენით correct_password ცვლადი და მასში შეინახეთ ნებისმიერი სთრინგი.
# სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შეეკითხეთ.
# საბოლოოდ, დაუბეჭდეთ access granted და ასევე რამდენჯერ მოუწია პაროლის შემოტანა.
# დაგჭირდებათ while loop, counter variable

correct_password = "12345678"  
user_gues = input("Enter password: ")
counter=0

while user_gues != correct_password:
    user_gues = input("Enter password: ")
    counter += 1
    
print("Access granted")
print("Your guess count:", str(counter))