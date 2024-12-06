# 8) Prompt the user to enter a password. Keep asking until they enter the correct password.

correct_password = "12345678"
user_input = input("Enter the password: ")

while user_input != correct_password:
    print("Incorrect password! Try again.")
    user_input = input("Enter the password: ")
print("Access!")
