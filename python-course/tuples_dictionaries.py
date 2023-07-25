# Tuples
tuple1 = (12345, 54321, 678910)

print(tuple1)
print(tuple1[2])

tuple2 = (tuple1[0], 13579, tuple1[1]) # tuples are immutable

print(tuple2)

# Dictionaries (key value)
dict = {"Firstname": "John", "Surname": "Doe"}

print("Hello!"+" "+dict["Firstname"]+" "+dict["Surname"])
dict.clear()