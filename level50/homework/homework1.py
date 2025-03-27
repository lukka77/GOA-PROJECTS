# 1)Prompt the user to enter a number. If the input is not a number, display an error message.

def get_number():
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        print(f"You entered the number: {number}")
    except ValueError:
        print("Error: Please enter a valid number.")