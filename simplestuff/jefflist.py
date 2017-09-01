#test for lists

jefflist = ['my', 'name', 'jeff']
print(jefflist[0])
print(jefflist[1])
print(jefflist[2])
print(' ')
print(jefflist[2] + ' ' + jefflist[0] + ' ' + jefflist[1])

succ = [[69, 420, 1337], ['succ', 'thicc', 'dix']]

print(succ)
print(succ[0][1]) #first list, second number

print(succ[-1][-1]) #negative is reverse
print(jefflist[-2] + ' ' + jefflist[-0] + ' ' + jefflist[-1])

print(jefflist[1:3]) #word 1 to 2, "name" "jeff"

print(jefflist * 3) #TRIPPLE THE JEFF
print(succ * 2)

jefflist[1] = 'meme' #change values within list
print(jefflist)
jefflist[-1] = 'the nutshack'
print(jefflist)

print(' ')

nogger = ['a', 'b' ,'c' , 'd']
print(nogger)
nogger = nogger + ['e', 'f', 'g', 'x']
print(nogger)
nogger = nogger + ['a', 'c', 'g', 'd']
print(nogger)
del nogger[1:5] #delets words
print(nogger)
