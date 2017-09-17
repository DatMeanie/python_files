#!python3
#randomizes classes for CSS websites. wont be pretty
#writes all information to a txt file. needs to be converted to .css
#also write a basic html file if you so wish
import random, os

classNumber = 1
turns = 1000 #how many classes to be made?

textalign = ["left", "center", "right", "nothing"]
bordercheck = ["yes", "no"]
borderstyle = ["solid", "groove", "dotted", "dashed", "double", "ridge", "inset", "outset"]
borderside = ["top", "right", "left", "bottom", "all"]

def ColorPicker():
    rgbcolor = [0, 0, 0]
    rgbcolor[0] = random.randint(0, 255)
    rgbcolor[1] = random.randint(0, 255)
    rgbcolor[2] = random.randint(0, 255)
    color = '#%02x%02x%02x' % (rgbcolor[0], rgbcolor[1], rgbcolor[2])
    return color

def RandomNumber():
    return str(random.randint(10, 30))

print('Congratulations! You just aquired the amazing website making machine. \nYou just need to convert the txt files this program will create and you got yourself a fancy website. \nContinue?')
input()
for x in range(0, turns):
    styleSheet = open('stylesheet.txt', 'a')
    styleSheet.write('p.class' + str(classNumber) + ' { ')
    styleSheet.write('\n color: ' + ColorPicker() + ';')
    styleSheet.write('\n font-size: ' + RandomNumber() + 'px;')
    styleSheet.write('\n letter-spacing: ' + RandomNumber() + 'px;')
    if int(RandomNumber()) > 15:
        styleSheet.write('\n background-color: ' + ColorPicker() + ';')
    if textalign[random.randint(0,3)] != 'nothing':
        styleSheet.write('\n text-align: ' + textalign[random.randint(0,2)] + ';')
    if bordercheck[random.randint(0,1)] != 'no':
        if borderside == 'all':
            styleSheet.write('\n border-style: ' + borderstyle[random.randint(0, 7)] + ';')
            styleSheet.write('\n border-color: ' + ColorPicker() + ';')
            styleSheet.write('\n border-width: ' + RandomNumber() + ';')
            if bordercheck[random.randint(0,1)] != 'no':
                styleSheet.write('\n border-radius: ' + str(random.randint(0,10)) + 'px;')
        else:
            border = borderside[random.randint(0,3)]
            styleSheet.write('\n border-' + border + '-style: ' + borderstyle[random.randint(0, 7)] + ';')
            styleSheet.write('\n border-' + border + '-color: ' + ColorPicker() + ';')
            styleSheet.write('\n border-' + border + '-width: ' + RandomNumber() + ';')
            if bordercheck[random.randint(0,1)] != 'no':
                styleSheet.write('\n border-radius: ' + str(random.randint(0,10)) + 'px;')
    styleSheet.write('\n } \n')
    classNumber += 1
styleSheet.close()

#CSS document done. HTML next
indexFile = open('index.txt', 'a')
indexFile.write('<html> \n <head> \n <link rel="stylesheet" type="text/css" href="stylesheet.css">\n <title>Why</title> \n </head> \n <body> \n')
for x in range(0, turns):
    indexFile.write('<p class=\"class' + str(x + 1) + '\"> text </p>\n')
indexFile.write('</body>\n</html>')
indexFile.close()
print('Done!')
input()
