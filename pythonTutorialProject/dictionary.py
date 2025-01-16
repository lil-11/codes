# dictionary is a collection of {key:value} pair,
# they're ordered and changeable
# no duplicates allowed

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# to get one of the values, get the key.
# if python doesn't get the key, it returns None
# print(capitals.get("USA"))

# you can add a new key:value pair / update using the update method
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})

# to remove a key:value pair, use the pop method, then pass in a key
# capitals.pop("China")

# to remove the latest inserted key:value pair, use the popitem method
# capitals.popitem()

#capitals.clear() # tp clear a dictionary

# to get the keys only, use
# keys = capitals.keys()
# print(keys)
#
# values = capitals.values()
# print(values)
#
# # to iterate over every key
# for key in capitals.keys():
#     print(key)
#
# for value in capitals.values():
#     print(value)

# for key, value in capitals.items():
#     print(f"{key}: {value}")
#
# print(capitals)


#Concession stand program
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0
print("----- MENU ------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- Your Order ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is ${total:.2f}")