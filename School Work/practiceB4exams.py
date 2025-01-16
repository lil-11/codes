amt = float(input("Enter amount: "))
if amt > 100000:
    discount_rate = 0.10 #10 percent = 0.10
    discount_price = amt * (1 - discount_rate)
    print(f"Discounted Price for {amt} at rate {discount_rate} is {discount_price}")