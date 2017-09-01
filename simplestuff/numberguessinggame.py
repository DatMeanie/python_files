import random

while True:
    secretNumber = random.randint(1, 40)
    print('I choose a number between 1 and 40')

    for guesssesTaken in range(1, 7):
        while True:
            try:
                print('Take a guess')
                guess = int(input())
                break
            except Exception:
                print('write numbers')
        if guess < secretNumber - 5:
            print('sorry bud, too low')
        elif guess > secretNumber + 5:
            print('sorry bud, too high')
        elif guess < secretNumber:
            print('sorry bud, it was almost right but too low')
        elif guess > secretNumber:
            print('sorry bud, it was almost right but too high')
        else:
            break

    if guess == secretNumber:
        print('wow, you did it. it took you ' + str(guesssesTaken) + ' tries to figure it out')
    else:
        print('nah bud, so many wrongs. the number was ' + str(secretNumber))
