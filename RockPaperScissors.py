import random
from time import sleep
print('ROCK,PAPER,SCISSORS\n ')
sleep(2)
print('The game is between you and the computer.\nYou have to choose between R(rock),P(paper) or S(scissors)')
print('The winner of each round gets 20 points.')
print('The player with maximum points wins.\n   All The Best!!  \n ')
sleep(4)
L = ['R', 'P', 'S']
dict={'R':'Rock', 'P':'Paper','S':'Scissor'}
# user=y
# computer=x
u = 0
c = 0


def result():
    global u
    global c
    if y == 'R' and x == 'P':
        c += 20
        print('Computer wins!\n  ')
    elif y == 'R' and x == 'S':
        u += 20
        print('You win!\n  ')
    elif y == 'R' and x == 'R':
        print('Tie!')
        pass
    elif y == 'S' and x == 'P':
        u += 20
        print('You win!\n  ')
    elif y == 'S' and x == 'R':
        c += 20
        print('Computer wins!\n  ')
    elif y == 'S' and x == 'S':
        print('Tie!')
        pass
    elif y == 'P' and x == 'S':
        c += 20
        print('Computer wins!\n  ')
    elif y == 'P' and x == 'R':
        u += 20
        print('You win!\n  ')
    elif y == 'P' and x == 'P':
        print('Tie!')
        pass

a=int(input('Enter the number of rounds you wish to play:'))
i = 1
while i <= a:
    print('Round', i)
    x = random.choice(L)
    y = input('Rock,Paper or scissor?')
    y = y.upper()
    print('Computer chooses', dict[x])
    result()
    i += 1
print('User score', '=', u)
print('Computer score', '=', c)
print(' ')
print('And the winner of the game is ....')
sleep(3)
if u > c:
    print('USER!')
elif u==c:
    print('TIE!!')
else:
    print('COMPUTER!')


