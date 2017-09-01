#! python3
#shelve module testing
import shelve

shelfFile = shelve.open('mydata')
cats = ['Jeff', 'Nogger', 'Skully']
shelfFile['cats'] = cats
shelfFile.close()
#shelve is closed and later reopened
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
#information is saved and loaded up again
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
