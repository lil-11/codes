num = 33
if num % 2 == 0:
    print("We're inside an if block")
    print("This given number {} is even.".format(num))
else:
    print("This given number {} is odd.".format(num))


topUp = ["tall", "short", "medium"]
height = "tall" in topUp
print(height)