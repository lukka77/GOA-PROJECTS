# საკლასო დავალება:
# Task: Division Calculator with Error Handling
# Ask the user to input two numbers: a numerator and a denominator.
# Attempt to divide the numerator by the denominator inside a try block.
# If the user inputs something that is not a number, catch the error and display a message using except.
# If the user attempts to divide by zero, raise a ValueError with a custom message.
# Regardless of what happens, use a finally block to print a message like “Operation complete.”

numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

try:
    print(numerator / denominator)
except ValueError:
        raise ValueError("Error: Cannot divide by zero")
except:
        print("Error:")
finally:
        print("Operation complete")