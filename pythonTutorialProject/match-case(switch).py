#Match-case statement (switch): An alternative to using many elif statements
#its cleaner and more readable


def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return  "It's Friday"
        case 7:
            return  "It's Saturday"
        case _:
            return "Not a valid day"

print(day_of_week("pizza"))


#code to check if a day is weekend
# "|" represents yhe or operator
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False

print(is_weekend("Friday"))

