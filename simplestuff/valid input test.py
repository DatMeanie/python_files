#valid input test
combined = {}
names = []
passwords = [] 
while True:
    while True:
        print('Enter name: ')
        name = input()
        if name.istitle():
            names.append(name)
            break
        elif name == 'knife party':
            print(combined)
        print('Enter your name properly!')
    while True:
        print('Enter in your password: ')
        password = input()
        if password.isalnum():
            passwords.append(password)
            break
        print('Use numbers and letters only!')
    print('Ok thank you!')
    for i in range(len(names)):
        namess = names[i]
        passwordss = passwords[i]
        combined[namess] = passwordss
    print(' ')
