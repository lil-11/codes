#functions
from random import choice


def happy_birthday(name, age):
    print(f"Happy birthday {name}, you're are {age} years old")
happy_birthday("kalson", 19)

    #return statements
def add(x, y):
    z = x + y
    return z
print(add(5,2))

def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last
full_name = create_name("Koh", "Karlson")
print(full_name)

#default arguments
def net_price(list, discount=0, tax=0.05):
    return list * (1 - discount) * (1 - tax)
print(net_price(500))

# import time
# def count(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
# count(0, 10)

#keyword arguments
def hello(greeting, title, first, last):
    print(f"{greeting} {title}. {first} {last}")
hello("Hello", last="Karlson", first="Koh", title="Mr")

#arbitrary arguments
#*args
#====
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,4,5,6))

#**kwargs
#======
def print_address(**kwargs):
    print()
    for value in kwargs.values():
        print(value)
    print()
    for key in kwargs.keys():
        print(key)
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_address(street="123 Fake St.",
              city="Buea",
              state="Cameroon",
              zip="43478")

#membership operator
print()
grades = {
    "Sandy": "A",
    "Ashley": "B",
    "Favor": "C"
}
student = "Sandy"
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")

#list comprehension
print()
triples = [x * 3 for x in range(1, 11)]
print(triples)
squares = [x * x for x in range(1, 11)]
print(squares)

fruits = ["apple", "banana", "orange", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [number for number in numbers if number >= 0]
print(positive_nums)
negative_nums = [number for number in numbers if number < 0]
print(negative_nums)

#match-case statements
print()
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
print(is_weekend("Friday"))









#banking program
print()
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Python Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Not a valid choice")

    print("Thankyou! Have a nice day")

if __name__ == '__main__':
    main()

