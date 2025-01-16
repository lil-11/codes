acc_balance = 150000


rent = 2500
medical = 500
utilities = 800
transport = 2000
interest = 1500
family = 5000

total_spent = rent + medical + utilities + transport + interest + family
print(f"Total spent is ${total_spent:,}")

stock = 1000
monthly_earnings = 20000
interest_sav = 150000 * (3/100)

total_income = monthly_earnings + stock + interest_sav
print(f"Total income is ${total_income:,}")

Total = total_income - total_spent
print(Total)

total_left = acc_balance - total_spent + total_income

print(f"total left ${total_left:,}")


