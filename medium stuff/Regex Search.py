#! python3
# Regex Search - Want to search for a specific thing inside txt and py files?
import re, os

print('Enter in a directory with txt files: ')
directory1 = str(input())
while True:
    try:
        directory2 = os.listdir(directory1)
        os.chdir(directory1)
        break
    except FileNotFoundError:
        print('Sorry, this directory does not exist')
        directory1 = str(input())

txtRegex = re.compile(r'[\s\w(\d)-,//}{]+.txt')
mo1 = txtRegex.findall(str(directory2))
print(str(len(mo1)) + ' editable files found')
print(mo1)
print('What shallt be searched for?')
search = str(input())
searchRegex = re.compile(search)

for filename in mo1:
    fileOpen = open(filename)
    content = fileOpen.read()
    mo2 = searchRegex.findall(content)
    print(str(len(mo2)) + ' matches was found in ' + filename)
input()
    
