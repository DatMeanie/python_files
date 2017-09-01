#! python3
# random trees maybe????

from PIL import Image
from PIL import ImageColor
import random

im = Image.open('treemap.jpg')
color = [[20, 85, 0], [47, 120, 24], [76, 156, 51], [255, 255, 255, 0]]

widht, height = im.size
for x in range(widht):
    for y in range(height):
        r = random.randint(0, 2)
        if r < 2:
            im.putpixel((x, y), (color[r][0], color[r][1], color[r][2]))
        if r = 2:
im.save('newtreemap.jpg')
