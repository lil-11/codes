balance = 5000
Card_No = int(input("Welcome to UBA Bank. Enter card number: "))
pwd = int(input("Enter PIN to be saved: "))

print("Saving...")
print("Saved")
print("===============================================================================================================")
print("Welcome once more to United Bank of Africa, Cameroon branch. Select from the list below to perform your action.")

while True:
    print(
        '''
        1.) Withdraw
        2.) Send
        3.) Check balance
        4.) Exit
        '''
    )
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))

        if amount > balance:
            print("Insufficient balance.")
        else:
            for attempt in range(3):
                pwd1 = int(input("Enter your password: "))
                if pwd1 == pwd:
                    balance -= amount
                    print(f"You have successfully withdrawn FCFA {amount} from your account. Your new balance is FCFA {balance}")
                    break
                else:
                    print("Wrong password. Try again")
            else:
                print("You have entered the wrong password multiple times. Try again later")
                break
            
    elif choice == 2:
        amount = float(input("Enter amount: "))
        accNumber = int(input("Enter receiver's account number: "))
        print(f"Checking for account number '{accNumber}' in the database...")
        if amount > balance:
            print("Insufficient balance.")
        else:
            for attempt in range(3):
                pwd1 = int(input("Enter your password: "))
                if pwd1 == pwd:
                    balance -= amount
                    print(f"You have successfully sent FCFA {amount} to account '{accNumber}'. Your new balance is FCFA {balance}")
                    break
                else:
                    print("Wrong password. Try again")
            else:
                print("You have entered the wrong password multiple times. Try again later")
                
    elif choice == 3:
        for attempt in range(3):
            pwd1 = int(input("Enter your password: "))
            if pwd1 == pwd:
                print(f"Your balance is FCFA {balance}")
                break
            else:
                print("Wrong password. Try again")
        else:
            print("You have entered the wrong password multiple times. Try again later")

    elif choice == 4:
        print("Thanks for coming through")
        break
    
    else:
        print("Invalid choice. Enter a valid input next time")

    response = input("Do you want to perform another transaction? (yes/no): ")
    if response.lower() != "yes":
        print("Thanks for using UBA Bank. Have a great day!")
        break