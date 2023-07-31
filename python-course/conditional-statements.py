num = int(input("Enter a number:\n"))

if num > 0:
    if num >= 15:
        print("high range +")
    else:
        print("low range +")
elif num < 0:
    if num <= -15:
        print("high range -")
    else:
        print("low range -")
else:
    print("zero!")