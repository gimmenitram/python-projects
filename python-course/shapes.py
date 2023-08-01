symbol = "+"
count = 7

for a in range(count):
    for b in range(count-a):
        print(" ", end='') # no new line (end=)
    print(symbol)
    symbol += "++"
    #print(count)
#print("--")
for x in range(count-1):
    for y in range(x+2):
        print(" ", end='')
    print(symbol[0:-4])
    symbol = symbol[0:-2]