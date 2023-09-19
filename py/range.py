#multiplication table
number = int(input("Enter number: "))
for i in range(1, 11):
    multiplier = number * i
    print(number, "*", i, "=", multiplier)
