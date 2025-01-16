
#string functions

# name = input("Enter your full name: ")

#get the length of a string, including spaces
# result = len(name)

#reurns the first occurrence of a giving character using indexing
# result = name.find(" ")

#if a value is not found, it returns -1

#reurns the last occurrence of a giving character using indexing
# result = name.rfind(" ")



#upper method to turn all characters in a string to uppercase
# name = name.upper()

#lower method to turn all characters in a string to lowercase
# name = name.upper()
# print(name)

#isdidgit() returns true or false, if the string contains only digits
# result = name.isdigit()

#isalpha() returns true or false, if the string contains only alphabetical keys
# result = name.isalpha()
# print(result)

# to find  a particular character, you can use the find method
# it returns -1 if no spaces are found
# result = name.find(" ")  ---> to check if there is an empty space



#exercise
#validate user input exercise
#username is no more than 12 characters
#username must not contain spaces
#username must not contain digits

# names = input("Enter your name: ")
# length = len(names)
# space = names.count(" ")
# alpha = names.isalpha()
# if (length <= 12 and space == 0) and alpha:
#     print(f"Welcome {names}")
# else:
#     print("Invalid name")


#ALTERNATIVE ANSWER
#==================

# username = input("Enter a username: ")
#
# if len(username) > 12:
#     print("Username cant be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username cant contain spaces")
# elif not username.isalpha():
#     print("Your username cant contain numbers")
# else:
#     print(f"Welcome {username}")



#String Indexing
#================
# string_name[start:end:step]
credit_card_number = "1234-5678-9012-3456"
print(credit_card_number[:4])
print(credit_card_number[5:9])
print(credit_card_number[15:])
print(credit_card_number[-1])

# step: prints every second character within the string
#to reverse a string, set the step to be -1
print(credit_card_number[::2])

