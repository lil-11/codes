print("====Python Script to print selected items in a list========")
list1 = ["Amstrong", "Efeti", "orion", "Sapeur",]
print("Your list has a total of", end=":")
print(len(list1), "items")
# collecting input from user : 
#syntax -- Var_Name = dataType(input("......message...."))
#data types -- specifies the type of data to be collected
# int -- integers(+tive and -tive), float/double -- real numbers
stop_index = int (input("How many items do you want to display? :"))
print("======================================")
print("the output is:")
print("======================================")
for item in range(stop_index):
       print(list1[item])
print("==== @ Landmark Tech Engineers ======")