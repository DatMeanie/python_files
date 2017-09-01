#test with in expression
bestmemes = ['ur mum', 'banana', 'my life']
point = 0
while True:
    print('guess my favorite memes (hint, there is 3)')
    name = input()
    if name not in bestmemes:
        print(str(name) + ' IS WRONG!!!!!')
    else:
        print('ye, ya got it')
        point = point + 1
    print(' ')
    if point == 3:
        print('wow, you got them all. much amazing')
        break
