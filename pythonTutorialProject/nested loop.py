#nested loop = a loop within another loop(outer, inner)


# for y in range(3):
#     for x in range(1, 10):
#         print(x, end="")  # "end=" to make the output to be on the same line
#     print()


#rectangle
rows = int(input("Enter the number rows: "))
columns = int(input("Enter the number columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()