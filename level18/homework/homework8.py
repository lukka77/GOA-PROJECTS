# 8) Create a while loop that asks the user to enter a password. 
# Keep asking until they enter the correct password "Goa best". 
# Also print the count of incorrect passwords.

correct_pas = "Goa best"
count = 0
user_password = input("Enter password: ")

while user_password != correct_pas:
     count += 1
     user_password = input("Enter password: ")
     print("Correct password!")
     print("You needed", count, "tries")