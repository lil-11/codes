# a function is a block of reusable code
# def function_name()

#basic syntax
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}")
#     print(f"You are {age} years old")
#     print()
#
# happy_birthday("kalson", 20)
# happy_birthday("joe", 30)
# happy_birthday("martin", 25)


#function to display invoice
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("BroCode", 34.56, "01/01")




#return statement == used to end a function
#                   and send a result back to the caller

# create full names
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
#
# full_name = create_name("koh", "karlson")
# print(full_name)


#   1.) Positional arguments
#   2.) Default arguments
#   3.) Keyword arguments
#   4.) Arbitrary arguments



# default arguments = a default value for certain parameters
                 # Default is used when an argument is omitted
                 # it makes your functions more flexible, reduces the number of arguments

#function to calculate a net price
# assuming the discount will always be about 0, and tax, 0.05, we can use default

# def net_price(list_price, discount=0, tax=0.05):
#     return  list_price * (1 - discount) * (1 + tax)
#
# print(net_price(400))
# print(net_price(500, 0, 0.05))



# count up timer
# default arguments should ne used after positional arguments
import time
# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
#
# count(30, 27)


#keyword argument = an argument precede by an identifier
      #                  helps with readability
        #                order of arguments doesn't matter

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")
#positional argument are first b4 any keyword argument
# hello("Hello", title="Mr.", last="Karlson", first="Koh")

#end keyword argument
# for x in range(1, 11):
#     print(x, end=" ")
#
# print()

#seperate keyword argument
# print("1", "2", "3", "4", "5", sep="-")


#function to generate a phone number
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
#
# phone_num = get_phone(country=237, area=675, first=724, last=464)
# print(phone_num)



# arbitrary argument
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#           * unpacking operator


#   *args
#   ======
# a calculator that can collect multiple inputs
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4))

# a function that takes down multiple names
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Dr.", "Spongebob", "Harold")


#   **kwargs
#   ========
# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)
#     print()
#     for key in kwargs.keys():
#         print(key)
#     print()
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     print()
# print_address(street="Mayor Street",
#               city="Buea",
#               zip="654321",
#               country="Cameroon")


# creating a shipping label

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    print()
    print("Another way of outputting this is ")
    #another way of outputting
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Reacher", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="123456")

