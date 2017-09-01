#rock paper scissor

import random, sys
def scissor(number):
    if number == 3:
        return 'scissor'
    elif number == 2:
        return 'paper'
    elif number == 1:
        return 'rock'

yourpoint = 0
enemypoint = 0
insults = 0

print('hello, want to play rock paper scissors?')
input()
print('good, lets begin')
print('how many rounds do you want to play?')
while True:
    try:
        number = input()
        number = abs(int(number))
        break
    except Exception:
        print('did you write a word? that does not work. try again')
print(' ')
print('write your choice and I show mine')

while True:
    response2 = input()
    r = random.randint(1, 3)
    computerPick = scissor(r)
    if computerPick == 'scissor' and response2 == 'rock':
        print('dam, you won. i chose scissor')
        yourpoint = yourpoint + 1
    elif computerPick == 'scissor' and response2 == 'scissor':
        print('wat, we chose the same one!')
    elif computerPick == 'scissor' and response2 == 'paper':
        print('wow, i won. my choice was scissor')
        enemypoint = enemypoint + 1
    elif computerPick == 'paper' and response2 == 'scissor':
        print('dam, you won. i chose paper')
        yourpoint = yourpoint + 1
    elif computerPick == 'paper' and response2 == 'paper':
        print('wat, we chose the same one!')
    elif computerPick == 'paper' and response2 == 'rock':
        print('wow, i won. my choice was paper')
        enemypoint = enemypoint + 1
    elif computerPick == 'rock' and response2 == 'paper':
        print('dam, you won. i chose rock')
        yourpoint = yourpoint + 1
    elif computerPick == 'rock' and response2 == 'rock':
        print('wat, we chose the same one!')
    elif computerPick == 'rock' and response2 == 'scissor':
        print('wow, i won. my choice was rock')
        enemypoint = enemypoint + 1
    elif insults > 4:
        sys.exit()
    else:
        print('you didnt even try.')
        insults = insults + 1
        enemypoint = enemypoint + 1
    print(' ')
    print(str(yourpoint) + ' - ' + str(enemypoint))
    number = number - 1
    print(str(number) + ' rounds left')
    print(' ')
    if number == 0 and yourpoint > enemypoint:
        print('you won this match, cheater')
        print('want to play again?')
        response = input()
        if response == 'yes':
            print('nice, how many rounds?')
            while True:
                try:
                    number = input()
                    number = abs(int(number))
                    break
                except Exception:
                    print('did you write a word? that does not work. try again')
            yourpoint = 0
            enemypoint = 0
            print(' ')
            print('write your choice and I show mine')
        else:
            sys.exit()
    elif number == 0 and yourpoint < enemypoint:
        print('haha, you lost this match. im too good')
        print('want to play again?')
        response = input()
        if response == 'yes':
            print('nice, how many rounds?')
            while True:
                try:
                    number = input()
                    number = abs(int(number))
                    break
                except Exception:
                    print('did you write a word? that does not work. try again')
            yourpoint = 0
            enemypoint = 0
            print(' ')
            print('write your choice and I show mine')
        else:
            sys.exit()
    elif number == 0 and yourpoint == enemypoint:
        print('lol, it became a draw.')
        print('want to play again?')
        response = input()
        if response == 'yes':
            print('nice, how many rounds?')
            while True:
                try:
                    number = input()
                    number = abs(int(number))
                    break
                except Exception:
                    print('did you write a word? that does not work. try again')
            yourpoint = 0
            enemypoint = 0
            print(' ')
            print('write your choice and I show mine')
        else:
            sys.exit()
