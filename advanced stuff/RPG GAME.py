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

while True: #loading system
    try: #loads savefile
        shelfFile = shelve.open(r'.\RPG Game Data\\' + name + '\\' + name) #checks if savefolder exists
        playerhealth = shelfFile['playerhealth'] #checks if save exists
        playerinventory = shelfFile['playerinventory']
        playerstamina = shelfFile['playerstamina']
        print(' ')
        break #loading done
    except FileNotFoundError: #no save folder? no problem
        os.makedirs(r'.\RPG Game Data\\' + name)
    except KeyError: #creates new character
        startplayerinventory = {'Rusty Sword': {'Damage': 10, 'Stamina': 30},
                                'Gold': { 'Amount': 10}}
        startplayerhealth = 100
        startplayerstamina = 100
        shelfFile['playerhealth'] = startplayerhealth #saves the info so the loop can continue
        shelfFile['playerinventory'] = startplayerinventory
        shelfFile['playerstamina'] = startplayerstamina

def showinventory(playerinv): #show inventory function
    print('Your inventory:')
    for k, v in playerinv.items(): #picks item from playerinventory
        if v.get('Amount'):
            print(str(k) + ': ' + str(v.get('Amount')))
        else:
            print(k)

def playerattack(playerinv, response, stamina):
        try:
            rattack = random.randint(playerinv[response, response + 20])
            global damaged
            damaged = rattack
        except Exception:
            print('Invalid action, try again')
    

while True:
    action = str(input())
    print(' ')
    try:
        if action == 'inventory':
            showinventory(playerinventory)
        elif action == playerinventory[action]:
            playerattack(playerinventory, action, playerstamina)
        else:
            print('Invalid action, try again')
            print(' ')
    except Exception:
        print('Invalid action, try again')
        print(' ')
