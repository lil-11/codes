

import math

#   exercise 1
#   calculate the area of a rectangle

"""
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area of the rectangle is {area}cm²")
"""



#   exercise 2
#   shopping cart program

"""
item = input("What item would you like to buy? ")
price = float(input(f"Enter the price for the {item}: "))
quantity = int(input(f"How many {item}/s do you want? "))

total = price * quantity
checkout = input(f"Your total is ${total}. Proceed to checkout? (yes/no) ").lower()

if checkout == "yes":
    print(f"You successfully purchased {quantity} {item}/s for ${price}")
else:
    print("BROKE NIGGA 😂 ")
"""



#   exercise 3
#   circumference and area of a circle

"""
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"From {radius}cm³ as radius, the circumference of the circle is {round(circumference, 2)}cm")
print(f"Also, the area of the circle is {round(area, 2)}cm²")
"""



#   exercise 4
#   hypothenus of a right-angle triangle

"""
opposite = float(input("Enter the opposite side: "))
adjacent = float(input("Enter the adjacent side: "))

hypothenus = math.sqrt((pow(opposite, 2)) + (pow(adjacent, 2)))

print(f"Taking {opposite}cm² as opposite and {adjacent}cm² as adjacent, the hypotenuse of this triangle is {round(hypothenus, 2)}cm²")
"""



#   exercise 5
#   python calculator

"""
operator = input("Enter an operator (+ * / -): ")
if operator == "+":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        if num1 > num2:
            result = num1 * num2
            print(f"{num1} / {num2} = {round(result, 2)}")
        else:
            print(f"{num1} cannot be greater than {num2}")
else:
    print(f"{operator} is not a valid operator. Bye☻")

"""


#   exercise 6
#   weight converter program

"""
weight = float(input("Enter the weight: "))
unit = input("Kilograms or Pounds? (K or L) ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid unit")
"""


#   exercise 7
#   validate user input exercise
#   -   username is not more than 12 characters
#   -   username must not contain spaces
#   -   username must not contain digits

"""
name = input("Enter your username: ")

if len(name) > 12:
    print("Username must not contain more than 12 characters")
elif not name.find(" ") == -1:
    print("Username must not contain spaces")
elif not name.isalpha():
    print("Username must not contain digits")
else:
    print(f"Welcome {name}")
"""



#   exercise 8
#   python compound interest

"""
principle = 0
rate = 0
time = 0
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant be less than zero")
    else:
        break
while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("Rate cant be less than zero")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cant be less than zero")
    else:
        break

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} years is ${total:.2f}")
"""



#countdown timer

"""
import time

my_time = int(input("Enter the countdown time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("TIME'S Up")
"""



#   exercise 9
#   shopping cart program

"""
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")
for food in foods:
    print(food, end=", ")

for price in prices:
    total = total + price
print()
print(f"Your total us ${total:.2f}")
"""



#   exercise 10
#   python quiz game

questions = ("How many elements are in the periodic table? ",
             "Which animal lays the largest eggs? ",
             "What is the most abundant gas in the Earth's atmosphere? ",
             "How many bones are in the human body? ",
             "Which planet in the solar system is the hottest")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------------")

print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score/len(questions) * 100)
print(f"Your score is {score}%")

