#! python3
#mad libs practice project
import os, re

print('Enter in a directory with txt files:')
directory1 = str(input())
while True:
    try:
        directory2 = os.listdir(directory1)
        os.chdir(directory1)
    except FileNotFoundError:
        print('Sorry, this directory does not exist')
        directory1 = str(input())
txtRegex = re.compile(r'[\s\w\d-]+[()[\]{}]?.txt')
mo1 = txtRegex.findall(str(directory2))
print(str(len(mo1)) + ' editable files found')
print(mo1)
wordRegex = re.compile('NOUN|ADJECTIVE|VERB|')

for filename in mo1:
    fileOpen = open(filename)
    content = fileOpen.read()
    fileOpen.close()
    fileOpen = open(filename, 'w')
    
