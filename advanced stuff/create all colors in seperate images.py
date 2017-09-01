from PIL import Image
from PIL import ImageColor
import os
im = Image.new('RGBA', (100, 100))
number = 0
try:
    for x in range(0, 255):
        for y in range(0, 255):
            for z in range(0, 255):
                for x2 in range(100):
                    for y2 in range(100):
                        im.putpixel((x2, y2), (x, y , z ))
                number = number + 1
                if number < 2000000:
                    while True:
                        try:
                            im.save('.\\im0-2000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im0-2000000')
                if number < 4000000 and number > 1999999:
                    while True:
                        try:
                            im.save('.\\im2000001-4000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im2000001-4000000')
                if number < 6000000 and number > 3999999:
                    while True:
                        try:
                            im.save('.\\im4000001-60000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im4000001-60000000')
                if number < 8000000 and number > 5999999:
                    while True:
                        try:
                            im.save('.\\im6000001-8000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im6000001-8000000')
                if number < 10000000 and number > 7999999:
                    while True:
                        try:
                            im.save('.\\im8000001-10000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im8000001-10000000')
                if number < 12000000 and number > 9999999:
                    while True:
                        try:
                            im.save('.\\im10000001-12000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im10000001-12000000')
                if number < 14000000 and number > 11999999:
                    while True:
                        try:
                            im.save('.\\im12000001-14000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im12000001-14000000')
                if number < 16000000 and number > 13999999:
                    while True:
                        try:
                            im.save('.\\im14000001-16000000\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im14000001-16000000')
                if number < 18000000 and number > 15999999:
                    while True:
                        try:
                            im.save('.\\im16000000up\\color' + str(number) + '.png')
                            break
                        except Exception:
                            os.makedirs('.\\im16000000up')
                
except Exception:
    print('Error')
    input()
    
