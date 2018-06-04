#!python3
#!/usr/bin/python
#fucks with textures in minecraft
from PIL import Image
import os, random, re

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

for folderName, subfolders, filenames in os.walk('.\\assets\\minecraft\\textures'):
    print('Current folder is ' + folderName)
    for filename in filenames:
        directory3 = os.path.abspath(filename)
        try:
            print(filename)
            im = Image.open(folderName + '\\' + filename)
            width, height = im.size
            im.getpixel((0,0))
            (0, 0, 0, 0)
            for x in range(width):
                for y in range(random.randint(0, height)):
                    im.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            im.save(folderName + '\\' + filename)
        except Exception:
            print('Not openable')
