#another test on how lists work
print('name the best memes')
memes = []
while True:
    print('write done when you are done')
    name = input()
    if name == 'done':
        break
    memes = memes + [name]
print('your top memes')
for name in memes:
    print('( ͡° ͜ʖ ͡°) ' + name)
if len(memes) < 15:
    print('wow, are these all you can think of? much amazing, much normie')
elif len(memes) >= 15:
    print('you really know your memes. damn')
