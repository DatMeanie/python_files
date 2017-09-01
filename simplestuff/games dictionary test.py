games = {'grand theft auto 5': 'sucks', 'payday 2': 'sucks', \
         'minecraft': 'sucks', 'roblox': 'sucks'}
while True:
    print('enter game name to get review')
    name = str(input())
    if name == '':
        break

    if name in games:
        print(games[name])
    else:
        print('no review of ' + name)
        print('what is your opinion of ' + name + ' ?')
        review = str(input())
        games[name] = review
        print('righto, database updated')
