symbol = "|"
count = 15

for a in range(count):
    for b in range(count-a):
        print(" ", end='') # no new line (end=)
    print(symbol)
    symbol += "||"