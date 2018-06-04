#! python3
#walking directory test
import os

print('Write in a directory:')
directory = str(input())
for folderName, subfolders, filenames in os.walk(directory):
    print('The current folder is ' + folderName)

    for subfolder in subfolder:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('File inside ' + folderName + ': ' + fileName)

    print(' ')
