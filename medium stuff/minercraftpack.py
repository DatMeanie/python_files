#! python3
# man skriver in dir till ett minecraft resourcepack och sedan ersätter ljudfiler
import re, os, shutil, random

soundDir = []

print('Enter Resource Pack')
directory1 = str(input())
while True:
    try:
        directory2 = os.listdir(directory1)
        print(directory2)
        os.chdir(directory1)
        break
    except FileNotFoundError:
        print('Sorry, this directory doesn\'t exist')
        directory1 = str(input())

dir1Regex = re.compile(r'minecraft/[\s\w(\d)-,//}{]+')
print('Enter Minecraft Index File')
while True:
    indexFile = input()
    test = os.path.isfile('.\\' + str(indexFile))
    if test == True:
        try:
            indexFile = open(indexFile)
            mo1 = indexFile.read()
            break
        except Exception:
            print('Try Again')
    else:
        print('Try Again')
        
dir2Regex = re.compile(r'minecraft/sounds/[\s(\w)-,//]+')
mo2 = dir2Regex.findall(str(mo1))
for matches in mo2:
    ye = os.path.isdir('.\\assets\\' + matches)
    if ye == False:
        os.makedirs('.\\assets\\' + matches)
    else:
        print('Folders already exists')
        break
    
print('Enter in directory to a sound file. Type nothing to end')
while True:
    soundItem = str(input())
    if soundItem == '':
        break
    soundDir.append('.\\' + soundItem)
    
print(soundDir)
input()
for folderName, subfolders, filenames in os.walk('.\\assets\\minecraft\\sounds'):
    print('Current folder is ' + folderName)
    shutil.copy(soundDir[random.randint(0, (len(soundDir) - 1))], '.\\' + folderName + '.ogg')












