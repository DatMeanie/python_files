#! python3
# made for tyrants and martyrs game

from PIL import Image
from PIL import ImageColor
import random
im = Image.open('heightmap.jpg')
widht, height = im.size
for x in range(widht):
    for y in range(height):
        im.putpixel((x, y), (random.randint(95, 120)))

#im = im.convert('L')
im.save('heightmap1.jpg')

im = Image.open('heightmap.jpg')
widht, height = im.size
for x in range(widht):
    for y in range(height):
        im.putpixel((x, y), (random.randint(1, 50)))

im.save('heightmap2.jpg')
