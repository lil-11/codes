# #collection is single variable used to store multiple values
# #list = [] ordered and changeable. duplicates ok
# #set = {} unordered and immutable, but add/remove OK. no duplicated
# #tuple = () ordered and unchangeable. duplicates ok. faster
#
# #operations performed on strings can also be performed on collections
# fruits = ["apple", "banana", "orange", "coconut"]
# print(fruits[::-1]) #to reverse the list
# print(fruits[::2]) #to skip every one element
#
# #you can also iterate over them collections
# for fruit in fruits:
#     print(fruit)
#
# #below are the different methods that we can use on collections
# print(dir(fruits))
#
# #count the number of elements
# print(len(fruits))
#
# #use "in" to check if a value is within a collection
# print("apple" in fruits)
# print("pineapple" in fruits)
#
# #add an element at the end of the list
# fruits.append("Watermelon")
#
# #to remove elements
# fruits.remove("Watermelon")
#
# #to add an element at a given index
# fruits.insert(0, "pear")
#
# #sort a list in alphabetical order
# fruits.sort()
#
# #reverse a list
# fruits.reverse()
#
# #to clear a list
# # fruits.clear()
#
# #count the number of times an element is found in a list since duplicates are ok
# print(fruits.count("apple"))
#
# print(fruits)
#
#
#
# #SETS
# #====
#
# #indexing cant be used on a set since they're unordered
#
# fruits = {"apple", "orange", "banana", "coconut"}
#
# #to add elements on the set,
# fruits.add("pineapple")
#
# #to remove the first element
# fruits.pop()
#
# #no duplicates
#
# print(fruits)
#
# #TUPLES
# #======
#
# #tuples are faster than list
# fruits  = ("apple", "orange", "banana", "coconut")
# #there are only 2 additional methods for tuples; count and index





#EXERCISE
#========

#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end=", ")

for price in prices:
    total += price
print()
print(f"Your total is {total}")