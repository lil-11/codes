import random

# to generate a random whole number in between 1 and 6 exclusively
# number = random.randint(1, 6)
# print(number)

# it also takes variables
# low = 1
# high = 100
# number = random.randint(low, high)
# print(number)

# to pick a random choice from a sequence
# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# print(option)

# to shuffle a sequence
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)




# number guessing game

"""
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python NUmber Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}: ")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print("Too low, try again!")
        elif guess > answer:
            print("Too high, try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}: ")
"""



# Rock Paper scissors game


options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing!")
