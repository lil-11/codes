

# check if someone is eligible to vote
# age = int(input("Enter your age: "))
# if age > 100:
#     print("You're too old to sign up")
# elif age >= 18:
#     print("You're now signed up!")
# elif age < 0:
#     print("you haven't been born yet")
# else:
#     print("You must be 18+")



#check if a user entered a name
# name = input("Enter your name: ")
# if name == "":
#     print("You did not enter a name")
# else:
#     print(f"Hello {name}")



#calculator program
# operator = input("Enter an operator + - * /) ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator")



# weight converter program
weight = float(input("Enter your weight: "))
unit = input("In Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = weight * 205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 205
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")
