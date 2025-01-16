# condition expression behaves similarly as the ternary operator

#syntax
# X if condition else y  ---> X and Y represents output

num = 5

#check if number is positive/negative
# print("Positive" if num > 0 else "Negative")

#check if number is even or odd
result = "Even" if num % 2 == 0 else "Odd"
print(result)


a = 6
b = 7

#outputs the bigger number
max_num = a if a > b else b
print(max_num)

#outputs the smaller number
min_num = a if a < b else b
print(min_num)