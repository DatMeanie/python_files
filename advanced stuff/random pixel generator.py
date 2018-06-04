#! python3
#randomly places grey pixels on image downwards

from PIL import Image
import os, random

print('Enter in folder with images')
while True:
    dirR = str(input())
    if os.path.isdir(dirR) == True:
        os.chdir(dirR)
        break
print(os.listdir(dirR))

print('Enter in image')
while True:
    picture = input()
    test = os.path.isfile('.\\' + str(picture))
    if test == True:
        break
    else:
        print('Try Again')
        
im = Image.open(picture)
width, height = im.size #open image
im.getpixel((0,0))
(0, 0, 0, 0)
for x in range(width):
    for y in range(random.randint(10, height)):
        im.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
for y in range(height):
    for x in range(random.randint(10, width)):
        im.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
for x in range(height):
    for y in range(random.randint(10, width)):
        im.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
for y in range(width):
    for x in range(random.randint(10, height)):
        im.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))

print('What do you want it called?')
name = input()
im.save(str(name) + '.png')

