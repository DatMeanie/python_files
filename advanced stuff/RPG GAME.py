#! python3
#simple old school rpg, improved from earlier versions
import shelve, os, random

killed = 0
monster = 'none'
damaged = 0

print('Enter you name:')
name = str(input())
print(' ')
print('Hello and welcome to the game ' + name + '!')
print('This is a simple old school RPG where you input simple commands to play')
print('Type help at any point in time to get help')
print(' ')
print('Continue?')
input()

while True: #loading system
    try: #loads savefile
        shelfFile = shelve.open(r'.\RPG Game Data\\' + name + '\\' + name) #checks if savefolder exists
        playerhealth = shelfFile['playerhealth'] #checks if save exists
        playerinventory = shelfFile['playerinventory']
        playerstamina = shelfFile['playerstamina']
        playerweapons = shelfFile['playerweapons']
        print(' ')
        break #loading done
    except FileNotFoundError: #no save folder? no problem
        os.makedirs(r'.\RPG Game Data\\' + name)
    except KeyError: #creates new character
        startplayerinventory = {'Gold': { 'Amount': 10}}
        startplayerweapons = {'Rusty Sword': {'Damage': 10, 'Stamina': 30}}
        startplayerhealth = 100
        startplayerstamina = 100
        shelfFile['playerhealth'] = startplayerhealth #saves the info so the loop can continue
        shelfFile['playerinventory'] = startplayerinventory
        shelfFile['playerweapons'] = startplayerweapons
        shelfFile['playerstamina'] = startplayerstamina

def showinventory(playerinv, playerwep): #show inventory function
    print('Your inventory:')
    for k, v in playerinv.items(): #picks item from playerinventory
        print(str(k) + ': ' + str(v.get('Amount')))
    print(' ')
    print('Your Weapons:')
    for k, v in playerwep.items():
        print(k + ': Damage: ' + str(v.get('Damage')) + ' Stamina: ' + str(v.get('Stamina')))

def playerattack(playerinv, response, stamina):
        try:
            rattack = random.randint(playerinv[response, response + 20])
            global damaged
            damaged = rattack
        except Exception:
            print('Invalid action, try again')

def encounters():
    global number
    number = random.randint(1, 4)
    if number == 1:
        print('You encountered a dragon!')
    elif number == 2:
        print('You encountered a troll!')
    elif number == 3:
        print('You encountered a wyvern!')
    elif number == 4:
        print('You encountered a bandit!')
    else:
        print('Error!')

def monsters():
    print('type stuff here in future')

while True:
    encounters()
    action = str(input())
    print(' ')
    if action == 'inventory':
        showinventory(playerinventory, playerweapons)
    elif action in playerinventory.items() == True: 
        playerattack(playerinventory, action, playerstamina) #write item, attack
    else:
        print('Invalid action, try again')
        print(' ')
