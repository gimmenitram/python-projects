import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input('Rock, Paper or Scissors?\n').casefold()

print(user_choice + ' vs ' + computer_choice)

if computer_choice == user_choice:
    print('TIE - competed with ' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN - competed with ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN - competed with ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN - competed with ' + computer_choice)
else:
    print('LOSE - competed with ' + computer_choice)