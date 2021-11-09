import random

roll = random.randint(1,6)
guess = int(input('Guess the number \n'))

if guess == roll:
    print('User wins')
else:
    print('User lost, roll was ' + str(roll))