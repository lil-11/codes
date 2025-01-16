#format specifiers = {value:flags} format a value bases on flags that are inserted
price1 = 3094094.1344
price2 = -98733.65
price3 = 12533.34

#to add a decimal point specifier use .2f
print(f"Price 1 is {price1: .2f}")

#to add space after a value is displaced, writedown the number of spaces after the colon
print(f"Price 2 is {price2:10}")

#to left justify a value, use <number, right justify == >, center align == ^
print(f"Price 3 is {price3:<10}")

#use , for a thousand seperator
print(f"Price is {price3:,}")




