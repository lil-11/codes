# list comprehension = A concise way to create lists in python
#                       Compact and easier to read than traditional loops
#                       [expression: for value in iterable if condition]

#traditionally, you can do this
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

#using list comprehension
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
print(doubles)
print(triples)
print(squares)


#strings
#=======
fruits = ["apple", "orange", "banana", "coconut"]

#to turn the list to uppercase using list comprehension,
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

#to take the first letter of each fruit and place within a new list
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


#conditions
#==========
nums = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]
even_nums = [num for num in nums if num % 2 == 0]
odd_nums = [num for num in nums if num % 2 == 1]
print(f"Positive numbers: {positive_nums}, Negative numbers: {negative_nums}")
print(f"Even numbers: {even_nums}, Odd Numbers: {odd_nums}")







