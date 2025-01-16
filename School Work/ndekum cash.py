# Variables based on the question
credit_score = 720
annual_income = 10_000_000  # in CFA
account_balance = 5_000_000  # in CFA
loan_amount = 20_000_000  # in CFA
loan_term_years = 5  # years
loan_term_months = loan_term_years * 12  # months
interest_rate = 5 / 100  # 5%
withdrawal_amount = 4_000_000  # in CFA
minimum_balance_for_perk = 5_000_000  # in CFA
account_age_years = 6  # years
monthly_expenses = 800_000  # in CFA

# 1. Is Mr. Nde Kum eligible for a loan based on his annual income?
is_eligible_for_loan = annual_income >= loan_amount

# 2. How much will Mr. Nde Kum pay in interest for the loan over the full term?
total_interest = loan_amount * interest_rate * loan_term_years

# 3. Can Mr. Nde Kum afford the monthly loan payment based on his monthly expenses?
monthly_loan_payment = (loan_amount + total_interest) / loan_term_months
can_afford_monthly_payment = account_balance >= monthly_loan_payment

# 4. Will Mr. Nde Kum still be eligible for the perk after making the withdrawal?
will_maintain_perk = (account_balance - withdrawal_amount) >= minimum_balance_for_perk

# 5. How much balance will remain in his account after the withdrawal?
remaining_balance_after_withdrawal = account_balance - withdrawal_amount

# 6. Has Mr. Nde Kum been with the bank for more than 5 years?
is_long_term_client = account_age_years > 5

# 7. What is the total amount Mr. Nde Kum will owe after 5 years, including interest?
total_amount_owed = loan_amount + total_interest

# 8. Can Mr. Nde Kum withdraw the 4,000,000 CFA and still meet the conditions for the perk?
can_withdraw_and_maintain_perk = (account_balance - withdrawal_amount) >= minimum_balance_for_perk

# 9. Is the loan amount greater than 10 times Mr. Nde Kum’s annual income?
is_loan_too_large = loan_amount > (10 * annual_income)

# 10. Is the transaction flagged as both "large" and "international" for further review?
transaction_flags = ["large", "local", "international"]
is_flagged_for_review = "large" in transaction_flags and "international" in transaction_flags

# 11. With monthly expenses of 800,000 CFA, how long can Mr. Nde Kum sustain his expenses for?
months_of_sustainability = account_balance // monthly_expenses

# 12. After subtracting the expense from his account balance, how much will Mr. Nde Kum be left with after 6 months?
balance_after_6_months = account_balance - (6 * monthly_expenses)

# 13. Is the transaction flagged as both "large" or "local" for further review?
is_flagged_large_or_local = "large" in transaction_flags or "local" in transaction_flags

# Outputs
print("1. Eligible for Loan:", is_eligible_for_loan)
print("2. Total Interest for Loan:", total_interest)
print("3. Can Afford Monthly Payment:", can_afford_monthly_payment)
print("4. Maintain Perk After Withdrawal:", will_maintain_perk)
print("5. Remaining Balance After Withdrawal:", remaining_balance_after_withdrawal)
print("6. Long-Term Client:", is_long_term_client)
print("7. Total Amount Owed After 5 Years:", total_amount_owed)
print("8. Can Withdraw and Maintain Perk:", can_withdraw_and_maintain_perk)
print("9. Loan Amount Greater Than 10x Annual Income:", is_loan_too_large)
print("10. Flagged for Review (Large and International):", is_flagged_for_review)
print("11. Months of Sustainability:", months_of_sustainability)
print("12. Balance After 6 Months:", balance_after_6_months)
print("13. Flagged for Review (Large or Local):", is_flagged_large_or_local)
