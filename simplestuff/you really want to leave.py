import sys
while True:
    print('exit to exit')
    response = input()
    if response == 'exit':
        print('do you really want to leave?')
        response = input()
        if response == 'exit':
            print('no, you are stuck here')
            response = input()
            if response == 'exit':
                print('I SAID YOU CANNOT LEAVE!!!')
                response = input()
                if response == 'exit':
                    sys.exit()
    print(' you type ' + response)
