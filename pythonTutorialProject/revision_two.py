# Python Mini Projects
# =====================
import random


# Number Guessing Game
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
is_running = True
guesses = 0

print("Welcome to Python Number Guessing Game")
print(f"Select a number in between {lowest_number} and {highest_number}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("Number is out of range")
            print(f"Please select a number in between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! The correct answer is {answer}")
            print(f"Your total number of guesses were {guesses}")
            is_running = False



    else:
        print("Invalid number")
        print(f"Please select a number in between {lowest_number} and {highest_number}")