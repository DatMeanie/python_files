import copy
ss = ['aa', 'ss', 'dd', '420']
cheese = copy.copy(ss) #copy is for copy of list
cheese[3] = 69
print(ss)
print(cheese)

lol = [ss, cheese]
meme = copy.deepcopy(lol) #deepcopy is for list within lists
meme[1][3] = 4343
print(lol)
print(meme)
