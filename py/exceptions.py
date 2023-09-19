#using exceptions to avoid error messages
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero. Enter a valid age")
except ValueError:
    print("Invalid age")