name = input("Enter your name: ")
if len(name) < 3:
    print(f"Name must be atleat 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")