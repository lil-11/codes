names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[0])

#there are negative index in python. that's, the last object can be given an index -1
print(names[-1])

#to print out a particular section of the code, you can use indexing, i.e
print(names[0:3]) #this will print out only john, bob and mosh


#this code find the largest number in a list
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

'''
#calculating sum and average using list
numbers = [20, 40, 5, 50, 60, 70]
sum = 0
for number in numbers:
    sum += number
print("Sum = ", sum)
print("Average = ", sum/len(numbers))
'''