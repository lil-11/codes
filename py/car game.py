command = ""  # Initialize variable to store user input
started = False  # Initialize variable to track if the car is started or not

while True:  # Start an infinite loop
    command = input("> ").lower()  # Prompt the user for input and convert it to lowercase
    
    if command == "start":  # If the user input is "start"
        if started:  # If the car is already started
            print("Car is already started")  # Display a message
        else:  # If the car is not started
            started = True  # Start the car
            print("Car started...")  # Display a message
            
    elif command == "stop":  # If the user input is "stop"
        if not started:  # If the car is already stopped
            print("Car is already stopped")  # Display a message
        else:  # If the car is not stopped
            started = False  # Stop the car
            print("Car stopped...")  # Display a message
            
    elif command == "help":  # If the user input is "help"
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)  # Display a help message
        
    elif command == "quit":  # If the user input is "quit"
        break  # Exit the infinite loop and end the program
        
    else:  # If the user input is not recognized
        print("Sorry, I don't understand")  # Display an error message