#this program oonverts your weight to kilogram or pounds
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":  #.upper converts the k to K
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
    #print(f"Weight in Lbs is {converted} kilos.")
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))