value1 = 0b11110000
value2 = 0b11001100

print(bin(value1)+"\n"+bin(value2))

print(bin(value1&value2))
print(bin(value1|value2)) # or

valueX = 0b00111100
checkValue = value1^value2
print(checkValue, "=", valueX, "therefore, is", checkValue==valueX)

print(bin(value1) + "\n" + bin(value2 >> 3) + "\n" + bin(value2))
print("\n" + bin(value1) + "\n" + bin(value1 << 2) + "\n" + bin(value2) + "\n")
checkValue2 = value1 << 2
print("0b1111000000", "==", value1)
print("0b11001100", "==", checkValue2, "\n")
print(value1, "therefore, is not equal (!=) to", checkValue2, "and is",value1==checkValue2)