import random

def roll_dice():
    roll = []
    i = 0
    while len(roll) < 2:
        roll.append(random.randint(1, 6))
        i += 1 # == (i = i + 1)
    return roll

def main():
    player1 = input("Player 1! Enter your name:\n")
    player1result = roll_dice()
    roll1 = player1result[0] + player1result[1]

    player2 = input("Player 2! Enter your name:\n")
    player2result = roll_dice()
    roll2 = player2result[0] + player2result[1]

    print(player1, 'rolled', player1result[0], 'and', player1result[1], ', total', roll1)
    print(player2, 'rolled', player2result[0], 'and', player2result[1], ', total', roll2)

    if roll1 > roll2:
        print(player1, 'wins!')
    elif roll1 < roll2:
        print(player2, 'wins!')
    else:
        print('TIE!')

main()