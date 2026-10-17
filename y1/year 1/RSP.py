import random

choices = ["paper", "scissors", "rock",]
user_choice = input("Choose rock, scissors or paper: ").lower()

if user_choice not in choices:
    print("Invalid input, Please choose one of the options.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie. Try again if want to win.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!!!")
    else:
        print("You lose... Try again")