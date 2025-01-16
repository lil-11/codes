

#input(): a function that prompts the user to enter data. returns the entered data as a string
#=============================================================================================
# name = input("Whats your name? ")
# age = int(input("How old are you? "))
# print(f"Hello {name}! You're {age} years old")

#exercise 1: Calculate the area of a rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# print(f"The area of the rectangle is {area}cm²")

#exercise 2: shopping cart program
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
#
# print(f"You have bought {quantity} x {item}/s")
# print(f"You're total is: ${total}")




#Matlibs game, a word game where you create a story by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today, i went to a {adjective1} zoo.")
print(f"In an exhibit, i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")