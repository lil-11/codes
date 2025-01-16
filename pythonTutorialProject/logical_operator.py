#logical operator evaluates multple conditions (or, and, not)

#weather program

temp = int(input("Whats the temperature today? "))
is_sunny = False

if temp > 28 and is_sunny:
    print("Its hot outside")
elif temp <= 0 and not is_sunny:
    print("Its cold outside")
elif 28 > temp > 0 and is_sunny:
    print("Its warm outside")
elif temp >= 28 and not is_sunny:
    print("Its Hot outside")