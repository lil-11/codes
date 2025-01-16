#for loops executes a block of code a fixed number of times

#basic to count to 10
# for x in range(1, 11):
#     print(x)

# countdown
# for x in reversed(range(1, 11)):
#     print(x)
# print("HAppy New Year")

# to count by 2(or a specific number), you'll need to add a third argument in the range function
# for counter in range(2, 21, 2):
#     print(counter)

# you can also iterate over a string
# credit_card_number = "1234-5678-9012-3456"
# for x in credit_card_number:
#     print(x)

# use of the continue statement: to skip a specific number, say 13
# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)







# countdown timer in python
#use the sleep function from the time module to sleep for a given amount of time
import time


# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1): #setting the step to -1 is same as reversed function. 0 represents where the countdown stops
#     print(x)
#     time.sleep(1)
# print("Time is Up")


# digital clock
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is Up")