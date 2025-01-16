#while executes some code while some condition remains true


#asks the user to enter at least a word

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")




#prompts user to enter a number in between 1 and 10

# num = int(input("Enter a number: "))
#
# while 1 > num > 10:
#     print(f"{num} is not valid, try again")
#     num = int(input("Enter a number: "))
# print(f"Your number is {num}")






#simple interest program

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant be equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("interest rate cant be equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time (in years) cant be equal to zero")
    else:
        break

total = principle * pow((1 + rate /100), time)

print(f"Balance after {time} years: ${total:.2f}")