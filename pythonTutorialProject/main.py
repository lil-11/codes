

#Variables
#=========

#strings
best_food = "pizza"
first_name = "Karlson"
print(f"Hello {first_name}, your best food is {best_food}")

#intergers
my_age = 19
quantity = 5
print(f"You're {my_age} years old and you bought {quantity} items")

#floats
price = 10.99
gpa = 3.2
print(f"Your gpa is {gpa} and you got ${price} for that")

#boolean
is_student = True
if is_student:
    print("You're a student")
else:
    print("You're not a student")




#Typecasting: converting a variable from one datatype to another
#===============================================================

#checking the type
print(type(first_name))
print(type(gpa))
print(type(my_age))
print(type(is_student))

#now typecasting
gpa = int(gpa)
print(gpa)

my_age = float(my_age)
print(my_age)

my_age = str(my_age)
print(my_age)
print(type(my_age))

first_name = bool(first_name)
print(first_name) #this can be used to check if a user enters data ina field. it returns true if there are values and false if there are no values
