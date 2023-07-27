var1 = 1
var2 = 2
var3 = 3

print(var1<var2 or var2>var3) # OR satisfies 1 condition
print(var1<var2 and var2>var3) # AND must satisfies all conditions
print(var1<var2 and var2<var3)
print(not(var1<var2 and var2<var3))

a1 = 2
a2 = 2
a3 = 3

print("\n")
print(a1 is a2)
print(a1 is a3)
print(a1 is not a3)

alist = [100, 250, 500, 750, 1000]
item = 500

print("\n")
print(item in alist)
print(item not in alist)