import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('Do you want - rock, paper, scissors\n')
if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('USER WINS' + ', computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('USER WINS' + ', computer had ' + computer_choice) 
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('USER WINS' + ', computer had ' + computer_choice)
else:
    print('Computer choice was ' + computer_choice + ', so Computer Wins')    


