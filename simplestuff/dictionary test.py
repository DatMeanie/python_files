#dictionaries
meme = {'funny': 'not funny', 'new': 'yes', 'offensive': 'no', '9gag meme': 'yes'}
print(meme['funny'])
print('is your meme offensive? ' + meme['offensive'])
nogger = {420: 'ss', 69: '33', 1939: '420'}
print('MY FAVORITE NUMBRE IS ' + nogger[1939]) #dictionaries use keys instead of numbers
print('is nogger = meme ? ' + str(nogger == meme))
cocoball = {1939: '420', 69: '33', 420: 'ss'} #no order within dictionaries
print('is nogger = cocoball ? ' + str(nogger == cocoball))
