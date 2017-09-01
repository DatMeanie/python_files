#fantasy game inventory system
import random

playerinventory = {'Gold': 0, 'Rope': 1, 'Torch': 2, 'Dagger': 1}
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
    for i in range(len(addeditems)):
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
    else:
        print('You killed some bandits')
        loot(playerinventory, banditloot)

print('Welcome to the game. Type help to see the help menu')
while True:
    response = input()
    print(' ')
    if response == 'inventory':
        showinventory(playerinventory)
    elif response == 'help':
        print('Type inventory to see your inventory and adventure to adventure')
    elif response == 'adventure':
        encounters()
        
