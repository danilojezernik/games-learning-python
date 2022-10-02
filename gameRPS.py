from random import randint

player = input('Player 1, make your move: ').lower()

rand_num = randint(0, 2)

if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print(f'Computer plays: {computer}')

if player == computer:
    print('it\'s a tie!')
elif player == 'rock':
    if computer == 'scissors':
        print('Player wins!')
    else:
        print('Computer wins!')
elif player == 'paper':
    if computer == 'rock':
        print('Player wins!')
    else:
        print('Computer wins!')
elif player == 'scissors':
    if computer == 'rock':
        print('Computer wins!')
    else:
        print('Player wins!')
else:
    print(f'{player} <-- is not a valid move. Use rock, paper or scissors instead!')
