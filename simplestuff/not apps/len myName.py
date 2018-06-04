#it asks for name, also in loop and got easter eggs. very funny

import sys
jeff = 'my name jeff'

while True:
    print('what is your name?')
    myName = input()
    print('nice to meet you, ' + myName)
    print('the length of your name is: ')
    print(len(myName))
    if len(myName) == 3:
        print('a triangle has 3 sides, are you illuminati?')
        response = input()
        if response == 'yes' or 'Yes':
            sys.exit()
        else:
            print('well, thats good')
    elif len(myName) == len(jeff):
        print('my name jeff contains 12 letters, are you jeff?')
        response = input()
        if response == 'yes' or 'Yes':
            print('hello jeff')
        else:
            print('wow, really? got my hopes up for no reason.')
    print(' ')
