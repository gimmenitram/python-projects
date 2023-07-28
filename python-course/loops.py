count = 10
num = 10

while(count>0):
    num -= 1
    print("+" * count + str(num+1))
    count -= 1

for x in range(1, 11):
    num += 1
    print("+" * x + str(num))

# new set
string1 = "hey"
for y in string1:
    print(y)

string2 = "you"
for z in string2:
    print(string2)

list1 = ["beautiful", "kind", "person"]
count1 = 0
for a in list1:
    count1 += 1
    print(a + " - " + str(count1))