#fantasy game inventory system
#this version include saving system
import random, shelve, os

print('What is your name?') #makes save folder just for you
name = str(input())
while True:
    try:
        shelfFile = shelve.open('.\\saves\\' + name + '\\' + name)
        playerinventory = shelfFile['playerinventory']
        break
    except FileNotFoundError: #if no saves folder exist this will create the dir
        os.makedirs('.\\saves\\' + name)
    except KeyError:    #if no user exists this will create a new profile
        startinginventory = {'Gold': 0, 'Rope': 1, 'Torch': 2, 'Dagger': 1}
        shelfFile['playerinventory'] = startinginventory

dragonloot = ['Gold', 'Rope', 'Sword']
banditloot = ['Gold', 'Gold', 'Gold', 'Bow', 'Dagger']
wolfloot = ['Wolf Pelt', 'Meat']

def showinventory(inventory):
    print('Your Items')
    totalitem = 0
    for k, v in inventory.items():
        print(str(k) + ': ' + str(v))
        totalitem = totalitem + int(v)
    print('Total number of Items: ' + str(totalitem))
    print(' ')

def loot(inventory, addeditems):
    for i in range(random.randint(0,len(addeditems))):
        try:
            print('Looted ' + str(addeditems[i]))
            item = addeditems[i]
            inventory[item] = inventory[item] + 1
        except Exception:   #new item is added
            inventory[item] = 1
    print(' ')
def encounters():
    r  = random.randint(0, 2)
    events = ['dragon', 'bandit', 'wolf']
    if events[r] == 'dragon':
        print('You slayed a dragon')
        loot(playerinventory, dragonloot)
    elif events[r] == 'wolf':
        print('A pack of wolves ambush you, but you kill them all')
        loot(playerinventory, wolfloot)
    elif events[r] == 'bandit':
        print('You killed some bandits')
        loot(playerinventory, banditloot)
print('Welcome to the game. Type help to see the help menu')
while True:
    response = input()
    print(' ')
    if response == 'inventory':
        showinventory(playerinventory)
    elif response == 'help':
        print('Type inventory to see your inventory and adventure to adventure.\nEnter save to save your progress.\nWrite exit to end the game')
    elif response == 'adventure':
        encounters()
    elif response == 'save':
        try:
            shelfFile['playerinventory'] = playerinventory
            shelfFile.close()
        except Exception:
            shelfFile
    elif response == 'exit':
        break
