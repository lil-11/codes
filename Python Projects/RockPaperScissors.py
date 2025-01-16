# Python Mini Projects
# =====================

import random

options = ("rock", "paper", "scissors")
is_running = True

print("Welcome to Python Rock Paper Scissors Game")

while is_running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        break
print("Thanks for playing")
