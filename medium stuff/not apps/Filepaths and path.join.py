#! python3
#important: OS X and Linux use / instead of windows \
#folder is a modern name for directory, but directory is still the prefered word in python
import os

print(os.path.join('user', 'documents', 'spam'))
ss = os.path.join('user', 'documents', 'spam')
print(ss)

pythonfiles = ['character classes.txt', 'Filepaths and path.join.py', 'pipe test.py', 'sub() function.py']
for filename in pythonfiles:
    aa = os.path.join('Users\elev\Google Drive\python files\medium tier', filename)
    print(aa)

print(' ')
print(os.getcwd()) #current working directory
os.chdir('C:\Windows\\System32') #changes directory
print(os.getcwd())

print('making directories...')
for i in range(3):
    os.makedirs('C:\\test folders\\my name jeff' + str(i))
