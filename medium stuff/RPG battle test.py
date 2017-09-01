#! python3
#old-school rpg style battle test, includes 2 variables, health and attack
import shelve, random, os

killed = 0
playerdamage = 0
print('Enter your name:')
name = str(input())
while True:
    try:
        shelfFile = shelve.open('.\\RPG Battle Data\\' + name + '\\' + name)
        playerhealth = shelfFile['playerhealth']
        playerattacks = shelfFile['playerattacks']
        playerstamina = shelfFile['playerstamina']
        print(' ')
        break
    except FileNotFoundError:
        os.makedirs('.\\RPG Battle Data\\' + name)
    except KeyError:
        startplayerattacks = {'Slash': {'Damage': 20, 'Stamina': 30},
                            'Chop': {'Damage':30, 'Stamina': 60},
                            'Stab': { 'Damage':10, 'Stamina': 15},
                            'Fap': { 'Damage': 0, 'Stamina': -50}}
        shelfFile['playerattacks'] = startplayerattacks
        startplayerhealth = 100
        startplayerstamina = 100
        startplayerinventory = {'Gold': 20, 'Sword': 1}
        shelfFile['playerhealth'] = startplayerhealth
        shelfFile['playerstamina'] = startplayerstamina
        shelfFile['playerinventory'] = startplayerinventory
        print('Use a mix of different attacks to defeat different enemies')
        print('Each attack got an average damage and how much stamina it uses')
        print('You get 20 stamina every turn')
        print('You can also save your progress by writing save')
        print('Continue?')
        input()

def showattacks(playerattacks):
    print(' ')
    print('Possible Attacks Options:')
    for k, v in playerattacks.items():
        print(k + ': ' + str(v.get('Damage')) + ' damage, ' + str(v.get('Stamina')) + ' stamina')

def writing(response):
    if response == 'Save':
        print('Saving...')
        return 'Save'
    elif response == playerattacks[response]:
        print('attack')
        attack(response1)

def attack(response):
    rattack = random.randint((playerattacks[response]['Damage'] - playerattacks[response]['Damage']), (playerattacks[response]['Damage'] + playerattacks[response]['Damage']))
    global playerdamage
    global playerstamina
    playerdamage = rattack
    print('You try to ' + response + ' the target')
    if playerstamina >= playerattacks[response]['Stamina']:
        print('You did ' + str(playerdamage) + ' damage')
        print(' ')
        playerstamina = playerstamina - playerattacks[response]['Stamina']
    else:
        print('You fail miserably as you don\'t have enough stamina')
        playerdamage = 0
        playerstamina = 0
        
def encounters():
    revent = random.randint(0, 2)
    events = ['Bandits', 'Dragon', 'Troll']
    global encounter
    global monster
    encounter = events[revent]
    if encounter == 'Bandits':
        print('You encounter a band of bandits')
        print(encounter + ' has 50 health')
        monster = {'Health': 50, 'Damage': 20}
    if encounter == 'Dragon':
        print('You encounter a dragon')
        print(encounter + ' has 80 health')
        monster = {'Health': 80, 'Damage': 30}
    if encounter == 'Troll':
        print('You encounter a cave troll')
        print(encounter + ' has 60 health')
        monster = {'Health': 60, 'Damage': 25}

def monsterattack(event, monster):
    monsterattack = monster['Damage']
    rattack = random.randint((monsterattack - monsterattack), (monsterattack + monsterattack))
    global win
    win = False
    global monsterhealth
    global allowance
    global playerdamage
    while True:
        try:
            if allowance == 1:
                break
        except Exception:
            monsterhealth = monster['Health']
            allowance = 1
    monsterhealth = monsterhealth - playerdamage
    if monsterhealth > 0:
        print(event + ' has ' + str(monsterhealth) + ' health left')
        global monsterdamaged
        monsterdamaged = rattack
        print(event + ' did ' + str(rattack) + ' damage to you')
        global playerhealth
        playerhealth = playerhealth - monsterdamaged
        if playerhealth > 0:
            print('You now have ' + str(playerhealth) + ' health left')
        elif playerhealth <= 0:
            print(' ')
            print('You died')
    elif monsterhealth <= 0:
        print('You defeated ' + event)
        win = True
    
while True:
    encounters()
    monsterhealth = monster['Health']
    print(encounter + ' has an average damage of ' + str(monster['Damage']))
    print(' ')
    print('What do you do?')
    while True:
        playerstamina = playerstamina + 20
        if playerhealth <= 0:
            print(str(killed) + ' creatures was slayed by you')
            print(' ')
            print('Restarting...')
            print(' ')
            playerhealth = 100
            playerstamina = 100
            break
        showattacks(playerattacks)
        print('You have ' +  str(playerstamina) + ' stamina left')
        print(' ')
        response1 = str(input())
        if response1 == 'Save':
            try:
                shelfFile['playerhealth'] = playerhealth
                shelfFile.close()
            except Exception:
                shelfFile
        writing(response1)
        monsterattack(encounter, monster)
        try:
            if win == True:
                print(' ')
                killed = killed + 1
                break
        except Exception:
            win = False
