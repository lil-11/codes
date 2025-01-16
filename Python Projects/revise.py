import random

def guess(x):
    randNum = random.randint(1, x)
    guess = 0
    while guess != randNum:
        guess = int(input("Guess a number: "))
        if guess < randNum:
            print("Too low")
        elif guess > randNum:
            print("Too high")
    print(f"Congrats. You guessed the number {randNum} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(f"Is {guess}  too high (h), too low (l) or correct (c)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess +1
    print("Congrats, the computer guessed the number correctly")


computer_guess(10)
