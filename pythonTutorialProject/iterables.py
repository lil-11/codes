# Iterables = An object/collection that can return its elements one at a time,
#           allowing it to be iterated over in a loop

numbers = (1 ,2 , 3, 4, 5)

for number in numbers:
    print(number, end=" ")
print()

#iterating backwards...
for number in reversed(numbers):
    print(number, end="-")
print()

#sets cant be reversed
fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit, end=" ")
print()

#iterating over a string of names
name = "Koh Karlson"
for characters in name:
    print(characters, end=" ")
print()

#dictionaries
my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}
for key, value in my_dictionary.items():
    print(f"{key}: {value}")




