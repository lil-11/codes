import random
import time


#User playing
def guess(x, guesses=0):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low, try again")
        elif guess > random_number:
            print("Too high, try again")

        guesses += 1

    print(f"Congrats!!! You guessed the random number, {random_number} correctly after {guesses} tries")


#Computer playing
def computer_guess(x, guesses=0):
    low = 1
    high = x
    print(f"Guess a number between {low} and {high}")
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #or high
        time.sleep(1)
        feedback = input(f"Is {guess} to high (H), too low(L) or correct(C)?: ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

        guesses += 1
    print(f"Congrats!!! The computer guessed the number, {guess} correctly after {guesses} tries")


computer_guess(10)