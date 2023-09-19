while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("This is a test app. Enter your choice by selecting the number: ")
    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("Sum: " + str(result))
    elif choice == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print("Difference: " + str(result))
    elif choice == "3":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
        print("Product: " + str(result))
    elif choice == "4":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Quotient: " + str(result))
    elif choice == "5":
        print("Bye")
        break
    else:
        print("Unknown choice. Try again.")
    response = str(input("Do you want to continue? (y/n): "))
    if response.lower() != "y":
        print("Have a nice day")
        break