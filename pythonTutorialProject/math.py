
import math

friends = 0
friends +=1       #augmented assignment operator
print(friends)


#build-in maths related functions
x = 3.14
y = -4
z = 5

#round function
# result = round(x)

#absolute value
# result = abs(y)

#power function
# result = pow(x, y)

# max function
# result = max(x, y, z)

# min function
# result = min(x, y, z)


# use this when you import the maths module
# 1.)  print(math.pi)  ---> PI constant
# 2.)  print(math.e)  ---> exponential constant
# 3.)  result = math.sqrt(x) ---> square root function
# 4.)  result = math.floor(x) ---> to round down
result = math.ceil(x)  #---> to round up

print(result)


#Exercise
# 1.) calculate the circumference of a circle
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference is {round(circumference, 2)}")

# 2.) area of a circle
# radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)}cm²")

# 3.) the Hypotenuse of a right angle triangle

print("Hypotenuse program")
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {round(c, 2)}")