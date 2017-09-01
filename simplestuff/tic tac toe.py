#tic tac toe
board = {'7': ' ', '8': ' ', '9': ' ', \
 '4': ' ', '5': ' ', '6': ' ', \
 '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
turn = 'X'
rounds = 0
while True:
    printBoard(board)
    print('Turn for ' + turn + '. Move on which space? Type restart to restart')
    move = input()
    if move == 'restart':
        board = {'7': ' ', '8': ' ', '9': ' ', \
         '4': ' ', '5': ' ', '6': ' ', \
         '1': ' ', '2': ' ', '3': ' '}
        rounds = 0
        print('restarting...')
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    rounds = rounds + 1
    if rounds == 9:
        printBoard(board)
        print('do you want to play again?')
        response = str(input())
        if response == 'yes':
            print('restarting...')
            rounds = 0
            board = {'7': ' ', '8': ' ', '9': ' ', \
             '4': ' ', '5': ' ', '6': ' ', \
             '1': ' ', '2': ' ', '3': ' '}
        else:
            break
