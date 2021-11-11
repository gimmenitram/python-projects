import random

roll = random.randint(1,6)
print("The computer have rolled " + str(roll))

guess = int(input("Guess the roll: \n"))

if guess == roll:
    print("You guessed it right! Roll was " + str(roll))
else:
    print("Too bad, the roll was " + str(roll))