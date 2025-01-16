user_purchase = float(input("Enter your purchase: "))

if user_purchase > 100000:
    discount = user_purchase * 0.1
    print(f"Amount after discount is FCFA {discount:.2f}")
elif 50000 < user_purchase < 100000:
    discount = user_purchase * 0.05
    print(f"Amount after discount is FCFA {discount:.2f}")
else:
    print(f"Amount after discount is FCFA {user_purchase:.2f}")