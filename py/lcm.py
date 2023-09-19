#lcm of 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
x = 0
while True:
    x += 1
    if not(x % num1 or x % num2):
        break
print(f"{x} is the LCM of {num1} and {num2}")