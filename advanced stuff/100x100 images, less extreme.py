#! python3

from PIL import Image
from PIL import ImageColor
im = Image.new('RGBA', (100, 100))
number = 0
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, 3*x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, x, x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (x, 3*x, x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (x, x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (x, 3*x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, 3*x, x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, 2*x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, x, x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (x, 3*x, x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (x, x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (x, 3*x, 3*x))
    number = number + 1
    im.save('color' + str(number) + '.png')
for x in range(0, 83):
    for x2 in range(100):
        for y2 in range(100):
            im.putpixel((x2, y2), (3*x, 3*x, x))
    number = number + 1
    im.save('color' + str(number) + '.png')
