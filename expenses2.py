total = 0
expenses = []

# Set approach (set to x5)

# for i in range(5):
#     expenses.append(float(input("Enter expense:")))
# total = sum(expenses)
# print("You spent $", total, " on lunch this week.", sep='')

# Declared frequency approach
num_expense = int(input("How many times did you spend?"))

for i in range(num_expense):
    x = i + 1
    expenses.append(float(input("Enter expense #" + str(x) + ": ")))
total = sum (expenses)
print("You spent $", total, " on lunch this week.", sep='')