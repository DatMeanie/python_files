#!python3
#turns chosen image into black and white

from PIL import Image
import os

print('Enter in folder with images')
while True:
    changeDir = str(input())
    if os.path.isdir(changeDir) == True:
        os.chdir(changeDir)
        break
    else:
        print('Invalid input, try again')

print(os.listdir(changeDir))

print('Enter in image')
while True:
      picture = input()
      if os.path.isfile('.\\' + str(picture)) == True:
          break
      else:
          print('Invalid input, try again')

im = Image.open(picture)
im = im.convert('L')
im.save('result.png')
