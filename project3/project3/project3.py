import random
play_again=True
choices=["rock", "paper", "scissors"]

#main while Cycle

while play_again == True:
    user_choice = input("Enter either rock paper or scissors: ").lower()
    while user_choice not in choices:
        print("invalid choise")
        user_choice = input("Enter either rock paper or scissors: ").lower()
    computer_choice = random.choice(choices)

#choices

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

#main if code block

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print("You win!")
    elif (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

#play again

    stop_playing=input("do you want to spot playing?: ").lower()
    if stop_playing =="yes":
        play_again = False
        print("thanks for playing!")
    elif stop_playing =="no":
        play_again = True