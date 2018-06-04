#tuples are like lists but not editable
tuplee = (1, 2, 3)
print(tuplee)
print(tuplee[1:3])
try:
    tuplee[2] = 2 #noneditable
except:
    print('tuplee[2] = 2 - this is wrong')
    print('cannot change value within tuples')
print(tuple([5, 6, 79])) #creats tuple from values passed into it
print(list((5, 6, 79))) #changes into list

