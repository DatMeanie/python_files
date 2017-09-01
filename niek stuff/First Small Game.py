print('You find yourself in an abandoned village, A big guy with an axe charges at you! What are you going to do?')
print('Fight back, Run.')
action = input()
if action == 'Fight back':
    print('You punch him in the face, enough to stun him for a couple seconds, you run into one of the buildings.')
    print('You find a gun on the table. Throw it, Shoot at the big guy.')
    actionx = input()
    if actionx == 'Throw it':
        print('You throw it in his face, He drops the big ax on the floor and the floor brakes beneath him,.')
        print('You survived, Well done.')
    elif actionx == 'Shoot it at the big guy':
          print('The gun doesnt have any ammo stupid, The big guy smashes you. The end.')
else:
    print('You try to run but he catches up too you. He smashes you with his big axe, you are now dead. Good job.')           
    
        
