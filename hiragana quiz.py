#!python3
# asks english sounds for japanese characters
# made for my japanese studies
# alphabet: Hiragana
import random

myList = { "1": { "English": "a", "Japanese": "あ"},
           "2": { "English": "i", "Japanese": "い"},
           "3": { "English": "u", "Japanese": "う"},
           "4": { "English": "e", "Japanese": "え"},
           "5": { "English": "o", "Japanese": "お"},
           "6": { "English": "ka", "Japanese": "か"},
           "7": { "English": "ki", "Japanese": "き"},
           "8": { "English": "ku", "Japanese": "く"},
           "9": { "English": "ke", "Japanese": "け"},
           "10": { "English": "ko", "Japanese": "こ"},
           "11": { "English": "ga", "Japanese": "が"},
           "12": { "English": "gi", "Japanese": "ぎ"},
           "13": { "English": "gu", "Japanese": "ぐ"},
           "14": { "English": "ge", "Japanese": "げ"},
           "15": { "English": "go", "Japanese": "ご"},
           "16": { "English": "sa", "Japanese": "さ"},
           "17": { "English": "shi", "Japanese": "し"},
           "18": { "English": "su", "Japanese": "す"},
           "19": { "English": "se", "Japanese": "せ"},
           "20": { "English": "so", "Japanese": "そ"},
           "21": { "English": "za", "Japanese": "ざ"},
           "22": { "English": "ji", "Japanese": "じ"},
           "23": { "English": "zu", "Japanese": "ず"},
           "24": { "English": "ze", "Japanese": "ぜ"},
           "25": { "English": "zo", "Japanese": "ぞ"},
           "26": { "English": "so", "Japanese": "そ"},
           "27": { "English": "ta", "Japanese": "た"},
           "28": { "English": "chi", "Japanese": "ち"},
           "29": { "English": "tsu", "Japanese": "つ"},
           "30": { "English": "te", "Japanese": "て"},
           "31": { "English": "to", "Japanese": "と"},
           "32": { "English": "da", "Japanese": "だ"},
           "33": { "English": "ji", "Japanese": "ぢ"},
           "34": { "English": "zu", "Japanese": "づ"},
           "35": { "English": "de", "Japanese": "で"},
           "36": { "English": "do", "Japanese": "ど"},}

print('Hello, how many times do you want to play?')
while True:
    try:
        turns = int(input())
        print(' ')
        break
    except Exception:
        print('Error! Try again')
        

for x in range(1, turns):
    randomWord = random.randint(1, 36) #random word order
    jap = myList[str(randomWord)]["Japanese"] #make me type less :-)
    eng = myList[str(randomWord)]["English"]
    print('What sound is equal to ' + jap + ' ?')
    tries = 0
    while True:
        answer = input()
        tries += 1 #3 tries and then you're out
        if answer == eng and tries <= 3:
            print('Correct!')
            print(' ')
            break
        elif answer != eng and tries < 3:
            print('Incorrect! ' + str(3 - tries) + ' tries left')
        elif answer != eng and tries >= 3:
            print('Incorrect! It was ' + eng)
            break
        
