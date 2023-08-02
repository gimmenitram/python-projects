def addition (num1, num2, num3):
    return num1 + num2 + num3

def subtraction (num1, num2):
    return num1 - num2

def multiplication (num1, num2):
    return num1 * num2

def division (num1, num2):
    if num2 == 0:
        return "Undefined"
    else:
        return num1 / num2
    
A = 5
B = 10
C = 0

addTotal = addition(A, B, C)
print("+ =", addTotal)

subTotal = subtraction(B, A)
print("- =", subTotal)

multTotal = multiplication(B, A)
print("* =", multTotal)

divTotal1 = division(B, A)
print("/1 =", divTotal1)

divTotal2= division(A, C)
print("/2 =", divTotal2)