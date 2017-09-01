#adding names to list test, with cats!

print('name my cats')
catnames = [] #the brackets indicate a list, even if it's empty
while True:
    print('enter name of cat ' + str(len(catnames) + 1) + ' (or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catnames = catnames + [name]
print('cats names are:')
for name in catnames:
    print(' ' + name)
